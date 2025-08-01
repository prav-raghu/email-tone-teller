from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="Sentiment API",
    description="Detects email tone, urgency, and suggests replies using OpenAI",
    version="1.0.0",
)

app.include_router(analyze_router)
