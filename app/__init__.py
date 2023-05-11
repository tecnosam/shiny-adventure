from fastapi import FastAPI

from app.routers import job, user, auth, service_provider


app = FastAPI()

app.include_router(job.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(service_provider.router)
