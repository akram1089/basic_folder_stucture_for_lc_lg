from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FastAPI + LangChain + LangGraph Basic Setup")
app.include_router(router)
