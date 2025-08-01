from fastapi import APIRouter, Depends, HTTPException
from backend.models.data.database_config import DatabaseConfig
from backend.services.admin.config_service import ConfigService

router = APIRouter(prefix="/admin/config", tags=["config"])

@router.get("/database")
async def get_database_config() -> DatabaseConfig:
    """Obtiene la configuración actual de las bases de datos"""
    service = ConfigService()
    return await service.get_database_config()

@router.put("/database")
async def update_database_config(config: DatabaseConfig) -> DatabaseConfig:
    """Actualiza la configuración de las bases de datos"""
    service = ConfigService()
    return await service.update_database_config(config)

@router.post("/database/test-postgres")
async def test_postgres_connection(config: DatabaseConfig) -> dict:
    """Prueba la conexión a PostgreSQL"""
    service = ConfigService()
    success = await service.test_postgres_connection(config.postgres)
    return {"success": success}

@router.post("/database/test-sqlserver")
async def test_sqlserver_connection(config: DatabaseConfig) -> dict:
    """Prueba la conexión a SQL Server"""
    service = ConfigService()
    success = await service.test_sqlserver_connection(config.sqlserver)
    return {"success": success}