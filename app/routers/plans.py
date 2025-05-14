from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import models
from ..database import get_db
from pydantic import BaseModel
import json

router = APIRouter()

class PlanCreate(BaseModel):
    name: str
    description: str
    permissions: list[str]
    limit: int

@router.post("/plans")
async def create_plan(plan: PlanCreate, db: AsyncSession = Depends(get_db)):
    new_plan = models.Plan(
        name=plan.name,
        description=plan.description,
        permissions=json.dumps(plan.permissions),
        limit=plan.limit
    )
    db.add(new_plan)
    await db.commit()
    await db.refresh(new_plan)
    print("New plan added!")  # debug
    return new_plan