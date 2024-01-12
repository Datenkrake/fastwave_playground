from fastapi import APIRouter
from endpoints import h2o_endpoint

router = APIRouter()
router.include_router(h2o_endpoint.router)