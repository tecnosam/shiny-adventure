from fastapi import APIRouter, Depends

from app.controllers import auth as controller

from app.forms.auth import (
    LoginForm,
    RegisterForm,
    UpdateProfileForm,
    ChangePasswordForm
)

from app.models.user import User

from app.dependencies.auth import get_current_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.put("/login")
async def login(form: LoginForm):

    return controller.login(**form.dict())


@router.post("/register")
async def register(form: RegisterForm):

    return controller.register(form.dict())


@router.put("/reset-password")
async def reset_password():
    return {"message": "Reset Password"}


@router.put("/change-password")
async def change_password(
    body: ChangePasswordForm,
    user_id: int = Depends(get_current_user)
):
    return controller.change_password(user_id, **body.dict())


@router.put("/update-user")
async def update_user(
    body: UpdateProfileForm,
    user_id: int = Depends(get_current_user)
):

    return controller.update_user(user_id, body.dict())


@router.get("/user", response_model=User)
async def get_user(user_id: int = Depends(get_current_user)):
    return controller.get_user(user_id)
