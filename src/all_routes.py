from fastapi import APIRouter

from src.email_password import app as email_password_router

router=APIRouter()

router.include_router(email_password_router, prefix="/email_password", tags=["email_password"])