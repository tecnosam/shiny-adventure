from fastapi import APIRouter, Path


router = APIRouter(prefix="/users", tags=["user"])


@router.get("/{user_id}/profile")
async def profile(user_id: int = Path(..., gt=0)):

    return {"message": "Profile"}
