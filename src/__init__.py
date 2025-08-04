import firebase_admin
from firebase_admin import credentials
import pyrebase
from dotenv import load_dotenv
load_dotenv()
import os


if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_auth_key.json")
    firebase_admin.initialize_app(cred)


# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID"),
    "databaseURL": os.getenv("DATABASE_URL")
}
firebase=pyrebase.initialize_app(firebaseConfig)