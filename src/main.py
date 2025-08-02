from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from loguru import logger
import uvicorn
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

from models import UserSignUp, UserLogin

app=FastAPI(docs_url="/")

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_auth_key.json")
    firebase_admin.initialize_app(cred)


# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
"apiKey": "AIzaSyBRBmltDdJViBxgWWfjNosemegDIByM9Ik",
"authDomain": "fastapi-auth-f9e5d.firebaseapp.com",
"projectId": "fastapi-auth-f9e5d",
"storageBucket": "fastapi-auth-f9e5d.firebasestorage.app",
"messagingSenderId": "324218522798",
"appId": "1:324218522798:web:f403b9ea9143e0fb0c313f",
"measurementId": "G-J8R0KT9391",
"databaseURL": ""
}
firebase=pyrebase.initialize_app(firebaseConfig)

@app.get('/get_all_emails')
def all_emails():
    users=auth.list_users()
    emails=[]
    for user in users.users:
        emails.append(user.email)
    return emails
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

if __name__== "__main__":
    uvicorn.run("main:app")