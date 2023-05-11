from pydantic import BaseModel
from typing import List


class Skill(BaseModel):

    id: int
    name: str


class ServiceProvider(BaseModel):

    userId: int
    tag: str

    skills: List[int] = []


class User(BaseModel):

    id: int

    name: str

    email: str
    phone: str

    address: str

    profilePictureURL: str

    serviceProvider: ServiceProvider = None
