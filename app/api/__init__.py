from fastapi import APIRouter
from .trades import router as trades_router

api_router = APIRouter()
api_router.include_router(trades_router)
