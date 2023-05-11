from fastapi import APIRouter, Path, Query

from app.forms.user import ServiceProviderForm


router = APIRouter(prefix="/service-providers", tags=["service-provider"])


@router.get("/{user_id}/profile")
async def profile(user_id: int = Path(..., gt=0)):

    return {"message": "Profile"}


@router.get("/{user_id}/skills")
async def get_skills(user_id: int = Path(..., gt=0)):
    # Fetch skills associated with a particular user
    return {"message": "Skills"}


@router.post("/create")
async def create_service_provider(body: ServiceProviderForm):

    return {"message": "Create"}


@router.patch("/add-skill")
async def add_skill(skill_id: int = Query(..., gt=0)):
    return {"message": "Add Skill"}


@router.patch("/remove-skill")
async def remove_skill(skill_id: int = Query(..., gt=0)):
    return {"message": "Remove Skill"}
