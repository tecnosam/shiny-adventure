from fastapi import APIRouter, Query, Path

from fastapi import HTTPException

from app.forms.job import JobForm, ApplicationForm, OrderForm

from app.models.job import Job

import app.controllers.job as controller

from typing import List


router = APIRouter(prefix="/jobs", tags=["job"])


@router.get("/list", response_model=List[Job])
async def get_job_list(
    skills: List[str] = Query(None, min_length=1, max_length=100),
    location: List[str] = Query(None, min_length=1, max_length=100),
    language: List[str] = Query(None, min_length=1, max_length=100),
):
    return controller.get_job_list(skills, location, language)


@router.get("/{job_id}", response_model=Job)
async def get_job(job_id: int = Path(..., gt=0)):

    response = controller.get_job(job_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return response


@router.post("/create")
async def create_job(body: JobForm):

    return controller.create_job(body)


@router.post("/{job_id}/apply")
async def apply_job(
    body: ApplicationForm,
    job_id: int = Path(..., gt=0),
):
    return controller.apply_job(body, job_id)


@router.post("/{job_id}/order")
async def order_job(
    body: OrderForm,
    job_id: int = Path(..., gt=0)
):
    return {"message": "Order"}


@router.delete("/{job_id}/delete")
async def delete_job(job_id: int = Path(..., gt=0)):

    return controller.delete_job(job_id)
