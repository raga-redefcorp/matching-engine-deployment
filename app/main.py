from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from dotenv import load_dotenv
import os
from app.routers import resume

# Load env variables
load_dotenv()

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

# Adds the router to the main app instance
app.include_router(resume.router)
    
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host=os.environ.get('HOST', "0.0.0.0"), port=port)