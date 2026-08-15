import socket
import threading
import json
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.task import ScanTask
from app.models.user import User
from app.schemas.task import ScanRequest, ScanResponse, TaskListResponse
from app.api.v1.endpoints.users import get_current_user

router = APIRouter(prefix="/scan", tags=["scan"])

def parse_ports(port_str: str):
    ports = []
    if "-" in port_str:
        start, end = map(int, port_str.split("-"))
        ports.extend(range(start, end + 1))
    else:
        for p in port_str.split(","):
            if p.strip():
                ports.append(int(p.strip()))
    return ports

def scan_ports(target: str, ports: list):
    open_ports = []
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(port,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return {
        "target": target,
        "open_ports": sorted(open_ports),
        "total_scanned": len(ports),
        "scanned_at": datetime.now().isoformat()
    }

def run_scan(task_id: int, target: str, ports_str: str):
    from app.core.database import SessionLocal
    db = SessionLocal()
    try:
        task = db.query(ScanTask).filter(ScanTask.id == task_id).first()
        if task:
            task.status = "running"
            db.commit()
        
        ports = parse_ports(ports_str)
        result = scan_ports(target, ports)
        
        if task:
            task.status = "completed"
            task.result = json.dumps(result)
            task.completed_at = datetime.now()
            db.commit()
    except Exception as e:
        if task:
            task.status = "error"
            task.error = str(e)
            db.commit()
    finally:
        db.close()

@router.post("/ports", response_model=ScanResponse)
def start_scan(
    request: ScanRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = ScanTask(
        user_id=current_user.id,
        task_type="port_scan",
        target=request.target,
        params=request.ports,
        status="pending"
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    
    thread = threading.Thread(
        target=run_scan,
        args=(task.id, request.target, request.ports)
    )
    thread.daemon = True
    thread.start()
    
    return ScanResponse(
        id=task.id,
        task_type=task.task_type,
        target=task.target,
        params=task.params,
        status=task.status,
        result=task.result,
        error=task.error,
        created_at=task.created_at,
        completed_at=task.completed_at
    )

@router.get("/{task_id}", response_model=ScanResponse)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(ScanTask).filter(
        ScanTask.id == task_id,
        ScanTask.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return ScanResponse(
        id=task.id,
        task_type=task.task_type,
        target=task.target,
        params=task.params,
        status=task.status,
        result=task.result,
        error=task.error,
        created_at=task.created_at,
        completed_at=task.completed_at
    )

@router.get("/", response_model=TaskListResponse)
def list_tasks(
    skip: int = 0,
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    tasks = db.query(ScanTask).filter(
        ScanTask.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    total = db.query(ScanTask).filter(ScanTask.user_id == current_user.id).count()
    return TaskListResponse(
        tasks=[ScanResponse(
            id=t.id,
            task_type=t.task_type,
            target=t.target,
            params=t.params,
            status=t.status,
            result=t.result,
            error=t.error,
            created_at=t.created_at,
            completed_at=t.completed_at
        ) for t in tasks],
        total=total
    )