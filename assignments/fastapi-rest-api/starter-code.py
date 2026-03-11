# Starter code for FastAPI REST API assignment

# Install FastAPI and Uvicorn before running:
# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Add more endpoints below for CRUD operations
