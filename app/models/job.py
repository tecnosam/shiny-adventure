from pydantic import BaseModel
from typing import List


class Application(BaseModel):

    id: int
    jobId: int
    userId: int
    price: float
    coverLetter: str

    appliedAt: str


class Job(BaseModel):

    id: int
    userId: int
    name: str
    description: str
    status: str
    minPrice: float
    maxPrice: float
    language: str
    location: str

    applications: List[Application] = []


class Order(BaseModel):

    id: int
    userId: int
    serviceProviderId: int

    price: float
    status: str

    createdAt: str
