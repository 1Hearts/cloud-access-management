from fastapi import FastAPI
from .routers import plans, subscriptions, access, services
from .database import engine, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Server started, DB checked.")# check server start 

app.include_router(plans.router)
app.include_router(subscriptions.router)
app.include_router(access.router)
app.include_router(services.router)

@app.get("/")
async def root():
    return {"message": "Cloud Access Management API is running"}