from fastapi import APIRouter

from controllers.papeis import papeis_controller as papeis

router = APIRouter()

router.include_router(papeis.router, prefix="/papeis")
