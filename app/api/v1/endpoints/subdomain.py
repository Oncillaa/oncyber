import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.v1.endpoints.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/subdomain", tags=["subdomain"])

class SubdomainRequest(BaseModel):
    domain: str

@router.post("/find")
def subdomain_find(request: SubdomainRequest, current_user: User = Depends(get_current_user)):
    domain = request.domain.strip()
    results = []
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=10)
        if r.status_code == 200:
            for line in r.text.strip().split("\n"):
                if "," in line:
                    sub, ip = line.split(",", 1)
                    results.append({"subdomain": sub, "ip": ip})
    except: pass
    return {"domain": domain, "subdomains": results[:20]}