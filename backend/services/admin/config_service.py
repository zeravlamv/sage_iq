from typing import Optional
from sqlalchemy import create_engine
from backend.models.data.database_config import DatabaseConfig, PostgresConfig, SQLServerConfig

class ConfigService:
    def __init__(self):
        self._config = None

    async def get_database_config(self) -> DatabaseConfig:
        """Obtiene la configuración actual de las bases de datos"""
        # TODO: Implementar lectura desde PostgreSQL
        pass

    async def update_database_config(self, config: DatabaseConfig) -> DatabaseConfig:
        """Actualiza la configuración de las bases de datos"""
        # TODO: Implementar actualización en PostgreSQL
        pass

    async def test_postgres_connection(self, config: PostgresConfig) -> bool:
        """Prueba la conexión a PostgreSQL"""
        try:
            url = f"postgresql://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
            engine = create_engine(url)
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {str(e)}")
            return False

    async def test_sqlserver_connection(self, config: SQLServerConfig) -> bool:
        """Prueba la conexión a SQL Server"""
        try:
            connection_string = (
                f"DRIVER={{{config.driver}}};"
                f"SERVER={config.host};"
                f"DATABASE={config.database};"
                f"UID={config.user};"
                f"PWD={config.password};"
                f"PORT={config.port};"
                f"TrustServerCertificate={str(config.trust_server_certificate)};"
                f"Encrypt={config.encrypt};"
                f"Authentication={config.authentication};"
                f"ConnectionTimeout={config.connection_timeout}"
            )
            url = f"mssql+pyodbc:///?odbc_connect={connection_string}"
            engine = create_engine(url)
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            print(f"Error al conectar a SQL Server: {str(e)}")
            return False