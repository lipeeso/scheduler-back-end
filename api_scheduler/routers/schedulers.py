from fastapi import APIRouter, Depends, HTTPException, Query, status



router = APIRouter()


@router.get("/schedulers", status_code=status.HTTP_200_OK)
async def get_schedulers():
    """
    Get all schedulers.
    """
    # Placeholder for actual implementation
    return {"message": "List of schedulers"}