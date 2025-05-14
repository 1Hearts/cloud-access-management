from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import json
from app.database import get_db
from app import models, database

router = APIRouter()

@router.get("/access/{user_id}/{api_request}")
async def check_access(user_id: int, api_request: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.Subscription)
        .options(selectinload(models.Subscription.plan))
        .where(models.Subscription.user_id == user_id)
    )
    sub = result.scalars().first()

    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")

    plan = sub.plan
    permissions = json.loads(plan.permissions)

    if api_request not in permissions:
        return {"message": "Access denied (check your plan permissions)"}

    if sub.usage >= plan.limit:
        return {"message": "Access denied: Usage limit exceeded."}

    return {"message": "Access granted (enjoy!)"}

@router.post("/usage/{user_id}")
async def track_usage(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.Subscription).where(models.Subscription.user_id == user_id)
    )
    sub = result.scalars().first()

    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")

    sub.usage += 1
    await db.commit()
    await db.refresh(sub)

    return {"message": "Usage recorded"}