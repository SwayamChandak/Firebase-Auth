from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from models import LoginRequest
from firebase_admin import auth
from loguru import logger
app=APIRouter()


@app.post('/auth/login')
def google_login(data: LoginRequest):
    try:
        token=auth.verify_id_token(data.id_token)
        uid=token["uid"]
        email=token["email"]
        logger.info(data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"access_token": data.id_token, "token_type": "bearer", "email": email}