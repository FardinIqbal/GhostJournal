from fastapi import FastAPI

from app.api import api_router

app = FastAPI(title='Ghost Journal')
app.include_router(api_router)
