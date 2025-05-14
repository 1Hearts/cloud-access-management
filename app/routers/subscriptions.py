from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import models
from ..database import get_db
from pydantic import BaseModel

router = APIRouter()

class SubscribeRequest(BaseModel):
    user_id: int
    plan_id: int

@router.post("/subscriptions")
async def subscribe(req: SubscribeRequest, db: AsyncSession = Depends(get_db)):
    plan = await db.get(models.Plan, req.plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    sub = models.Subscription(user_id=req.user_id, plan_id=req.plan_id, usage=0)
    db.add(sub)
    await db.commit()
    await db.refresh(sub)
    print("User subscribed!")  # debug
    return sub