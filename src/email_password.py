from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from firebase_admin import auth

from dotenv import load_dotenv

load_dotenv()
import os


from fastapi import Request
import requests
from loguru import logger
from src import firebase
from src.models import UserSignUp, UserLogin, EmailRequest
app=APIRouter()

FIREBASE_API_KEY = os.getenv("API_KEY")

@app.get('/get_all_emails')
def all_emails():
    users=auth.list_users()
    emails=[]
    for user in users.users:
        emails.append(user.email)
    return emails


def reset_password_mail(email: str):
    try:
        url=f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_API_KEY}"
        payload={
            "requestType": "PASSWORD_RESET",
            "email": email,
        }

        response=requests.post(url=url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
@app.post("/reset_password")
def reset_password(email: EmailRequest):
    try:
        mail=email.email
        result=reset_password_mail(mail)
        return JSONResponse(content={"message": f"Password Reset Email sent to {mail}"})
    except requests.HTTPError as e:
        return HTTPException(status_code=400, detail=e.response.json())

@app.post('/signup')
def create_user(user:UserSignUp):
    print(user.email)
    print(user.password)
    email=user.email
    password=user.password

    try:
        #create user in firebase, auth is inbuilt command by firebase_admin
        user=auth.create_user(email=email,
                         password=password)

        return JSONResponse(content={"message": f"User Account Created Successfully for {user.uid}"},
                            status_code=201)
    except auth.EmailAlreadyExistsError as e:
        logger.error(str(e))
        return HTTPException(status_code=400, detail=str(e))

@app.post('/login')
def get_access_key(user:UserLogin):
    email=user.email
    password=user.password
    try:
        user=firebase.auth().sign_in_with_email_and_password(email=email, password=password)
        token=user["idToken"]
        return token
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
        # return HTTPException(status_code=400, detail="Invalid Login Credentials")

@app.post('/check_access_key')
def validate_key(request:Request):
    header=request.headers
    jwt=header.get('authorization')

    user=auth.verify_id_token(id_token=jwt)

    return user["user_id"]