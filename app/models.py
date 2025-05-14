from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Subscription Plan table 
class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    permissions = Column(Text)
    limit = Column(Integer, nullable=False)

# user table
class Subscription(Base):
    __tablename__ = "subscriptions"

    user_id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    usage = Column(Integer, default=0)

    plan = relationship("Plan")