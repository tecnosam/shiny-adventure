from pydantic import BaseModel
from typing import List


class ServiceProviderForm(BaseModel):
    """
        Form for creating a service provider
    """
    tag: str

    # List of IDs of skills
    skills: List[int]
