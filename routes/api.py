from fastapi import APIRouter
from routes import ruta

api_router=APIRouter()
api_router.include_router(ruta.router,tags=["Prueba"],prefix="/prueba")