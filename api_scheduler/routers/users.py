from fastapi import APIRouter, Depends, HTTPException, Query, status

router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK)
async def get_users(): 
    return {"message": "List of users"}