from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import models
from ..database import get_db
import json

router = APIRouter()

@router.get("/access/{user_id}/{api_request}")
async def check_access(user_id: int, api_request: str, db: AsyncSession = Depends(get_db)):
    sub = await db.get(models.Subscription, user_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    plan = sub.plan
    permissions = json.loads(plan.permissions)

    if api_request not in permissions:
        return {"message": "Access denied: You do not have permission to this API."}

    if sub.usage >= plan.limit:
        return {"message": "Access denied: Usage limit exceeded."}

    return {"message": "Access granted (enjoy!)"}