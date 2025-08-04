from fastapi import FastAPI
import uvicorn

from src.all_routes import router as all_routes
from dotenv import load_dotenv
import os

load_dotenv()
app=FastAPI(docs_url="/")

app.include_router(all_routes)

if __name__== "__main__":
    uvicorn.run("main:app")