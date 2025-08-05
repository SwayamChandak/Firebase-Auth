from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.all_routes import router as all_routes
from dotenv import load_dotenv
import os

load_dotenv()
app=FastAPI(docs_url="/")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Or ["POST", "GET", "OPTIONS"]
    allow_headers=["*"]
)
app.include_router(all_routes)

if __name__== "__main__":
    uvicorn.run("main:app")