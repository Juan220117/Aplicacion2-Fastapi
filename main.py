from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api import api_router

app = FastAPI(title="Estudiantes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router,prefix="/estudiantes")