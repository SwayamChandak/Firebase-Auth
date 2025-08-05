from fastapi import APIRouter

from src.email_password import app as email_password_router
from src.google import app as google_router

router=APIRouter()

router.include_router(email_password_router, prefix="/email_password", tags=["email_password"])
router.include_router(google_router, prefix="/google", tags=["google"])
# router.include_router(email_password_router)
