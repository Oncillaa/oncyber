import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.v1.endpoints.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/steam", tags=["steam"])

STEAM_API_KEY = "D3A852E8AE5238CF6AEDED37F9D7AC93"

class SteamRequest(BaseModel):
    steam_id: str

@router.post("/stats")
def steam_stats(request: SteamRequest, current_user: User = Depends(get_current_user)):
    steam_id = request.steam_id.strip()
    profile = {}
    achievements = []

    try:
        r = requests.get(
            f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
            f"?key={STEAM_API_KEY}&steamids={steam_id}",
            timeout=10
        )
        if r.status_code == 200:
            players = r.json().get("response", {}).get("players", [])
            if players:
                p = players[0]
                profile = {
                    "steamid": p.get("steamid"),
                    "personaname": p.get("personaname"),
                    "profileurl": p.get("profileurl"),
                    "avatar": p.get("avatar"),
                    "avatarfull": p.get("avatarfull"),
                    "personastate": p.get("personastate"),
                    "lastlogoff": p.get("lastlogoff")
                }
    except: pass

    try:
        r = requests.get(
            f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"
            f"?key={STEAM_API_KEY}&steamid={steam_id}&appid=730",
            timeout=10
        )
        if r.status_code == 200:
            for a in r.json().get("playerstats", {}).get("achievements", [])[:10]:
                achievements.append({
                    "name": a.get("apiname"),
                    "achieved": a.get("achieved") == 1
                })
    except: pass

    return {"steam_id": steam_id, "profile": profile, "achievements": achievements}