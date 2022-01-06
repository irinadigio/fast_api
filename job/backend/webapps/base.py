from fastapi import APIRouter

from webapps.jobs import route_job

api_router = APIRouter()

api_router.include_router( route_job.router, prefix="", tags=["homepage"] )
