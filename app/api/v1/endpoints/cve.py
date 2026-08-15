import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.v1.endpoints.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/cve", tags=["cve"])

class CVERequest(BaseModel):
    product: str

@router.post("/search")
def cve_search(request: CVERequest, current_user: User = Depends(get_current_user)):
    product = request.product.strip()
    try:
        r = requests.get(f"https://cve.circl.lu/api/last/{product}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            return {"product": product, "cves": data[:10] if isinstance(data, list) else [data]}
    except: pass
    return {"product": product, "cves": []}