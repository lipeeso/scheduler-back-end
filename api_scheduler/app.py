from fastapi import FastAPI, status
from api_scheduler.routers import schedulers, users






app = FastAPI()

app.include_router(
    router= schedulers.router,
    prefix="/api/v1",
    tags=["Schedulers"],
)

app.include_router(
    router= users.router,
    prefix="/api/v1",
    tags=["Users"]
)


'''infra'''
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"message": "Welcome to the API Scheduler!"} 