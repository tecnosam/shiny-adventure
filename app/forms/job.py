from pydantic import BaseModel


class JobForm(BaseModel):
    name: str
    description: str
    minPrice: float
    maxPrice: float
    language: str
    location: str


class ApplicationForm(BaseModel):
    price: float
    coverLetter: str


class OrderForm(BaseModel):
    jobId: int
    serviceProviderId: int
    price: float
