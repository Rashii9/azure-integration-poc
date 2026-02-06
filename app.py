from fastapi import FastAPI
import os

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "local")

@app.get("/")
def read_root():
    return {
        "message": "Hello from Azure Integration POC",
        "environment": APP_ENV
    }

@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "Azure Integration Basic POC"
    }