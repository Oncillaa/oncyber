import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.v1.endpoints.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/osint", tags=["osint"])

class OSINTRequest(BaseModel):
    query: str

@router.post("/search")
def osint_search(request: OSINTRequest, current_user: User = Depends(get_current_user)):
    query = request.query.strip()
    results = {}

    # GitHub
    try:
        r = requests.get(f"https://api.github.com/users/{query}", timeout=5)
        if r.status_code == 200:
            data = r.json()
            results["github"] = {
                "login": data.get("login"),
                "name": data.get("name"),
                "bio": data.get("bio"),
                "public_repos": data.get("public_repos"),
                "followers": data.get("followers"),
                "following": data.get("following"),
                "created_at": data.get("created_at"),
                "url": data.get("html_url")
            }
    except: pass

    if "@" in query:
        try:
            r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}", timeout=5)
            if r.status_code == 200:
                results["hibp"] = r.json()
            elif r.status_code == 404:
                results["hibp"] = {"message": "Not found in any breaches"}
        except: pass

    return results