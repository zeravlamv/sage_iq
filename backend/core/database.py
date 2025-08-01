from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from backend.models.data.database_config import DatabaseConfig

Base = declarative_base()

class DatabaseManager:
    def __init__(self):
        self._postgres_engine = None
        self._sqlserver_engine = None
        self._config = None

    def configure(self, config: DatabaseConfig):
        """Configura las conexiones a las bases de datos"""
        self._config = config
        self._setup_postgres()
        # SQL Server se configurará cuando sea necesario

    def _setup_postgres(self):
        """Configura la conexión a PostgreSQL"""
        if not self._config:
            return

        postgres = self._config.postgres
        url = f"postgresql://{postgres.user}:{postgres.password}@{postgres.host}:{postgres.port}/{postgres.database}"
        self._postgres_engine = create_engine(url)
        return self._postgres_engine

    def _get_sqlserver_url(self):
        """Genera la URL de conexión para SQL Server"""
        if not self._config:
            return None

        sqlserver = self._config.sqlserver
        connection_string = (
            f"DRIVER={{{sqlserver.driver}}};"
            f"SERVER={sqlserver.host};"
            f"DATABASE={sqlserver.database};"
            f"UID={sqlserver.user};"
            f"PWD={sqlserver.password};"
            f"PORT={sqlserver.port};"
            f"TrustServerCertificate={str(sqlserver.trust_server_certificate)};"
            f"Encrypt={sqlserver.encrypt};"
            f"Authentication={sqlserver.authentication};"
            f"ConnectionTimeout={sqlserver.connection_timeout}"
        )
        return f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"

    def get_postgres_session(self):
        """Obtiene una sesión de PostgreSQL"""
        if not self._postgres_engine:
            self._setup_postgres()
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._postgres_engine)
        return SessionLocal()

# Instancia global del administrador de bases de datos
db_manager = DatabaseManager()