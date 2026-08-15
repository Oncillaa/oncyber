from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Any

class ScanRequest(BaseModel):
    target: str
    ports: str

class ScanResponse(BaseModel):
    id: int
    task_type: str
    target: str
    params: Optional[str] = None
    status: str
    result: Optional[str] = None
    error: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

class TaskListResponse(BaseModel):
    tasks: List[ScanResponse]
    total: int