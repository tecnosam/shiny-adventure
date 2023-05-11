from pydantic import BaseModel


class LoginForm(BaseModel):
    email: str
    password: str


class RegisterForm(BaseModel):

    name: str

    email: str
    phone: str

    address: str

    password: str

    profilePictureURL: str = 'https://i.imgur.com/2xVXWVW.png'


class UpdateProfileForm(BaseModel):

    name: str = None

    email: str = None
    phone: str = None

    address: str = None

    profilePictureURL: str = None


class ChangePasswordForm(BaseModel):

    password: str
