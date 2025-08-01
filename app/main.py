from fastapi import FastAPI
from app.database.base import postgres_engine, Base

app = FastAPI(title="SAGE IQ API")

@app.on_event("startup")
async def startup():
    # Create PostgreSQL tables only
    Base.metadata.create_all(bind=postgres_engine)

@app.get("/")
async def root():
    return {
        "message": "SAGE IQ API is running",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "databases": {
            "postgresql": "configured",
            "sqlserver": "pending_configuration"
        }
    }