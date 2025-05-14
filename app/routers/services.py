from fastapi import APIRouter

router = APIRouter()

@router.get("/service1")
async def service1():
    return {"message": "Service 1 - Cloud File Storage"}

@router.get("/service2")
async def service2():
    return {"message": "Service 2 - Cloud Video Processing"}

@router.get("/service3")
async def service3():
    return {"message": "Service 3 - Cloud Image Recognition"}

@router.get("/service4")
async def service4():
    return {"message": "Service 4 - Cloud Translation"}

@router.get("/service5")
async def service5():
    return {"message": "Service 5 - Cloud Email API"}

@router.get("/service6")
async def service6():
    return {"message": "Service 6 - Cloud Analytics API"}