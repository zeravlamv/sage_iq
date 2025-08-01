from fastapi import FastAPI
from backend.routers.admin import config
from backend.core.database import db_manager, Base

app = FastAPI(title="SAGE IQ API")

# Incluir routers
app.include_router(config.router)

@app.on_event("startup")
async def startup():
    """Inicialización de la aplicación"""
    # Por ahora, solo creamos las tablas en PostgreSQL
    # La configuración de SQL Server se hará desde la interfaz administrativa
    engine = db_manager._setup_postgres()
    Base.metadata.create_all(bind=engine)

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