from pydantic_settings import BaseSettings
from typing import Optional

class SQLServerSettings(BaseSettings):
    USER: str = ""
    PASSWORD: str = ""
    HOST: str = ""
    PORT: int = 1433
    DATABASE: str = ""
    DRIVER: str = "ODBC Driver 17 for SQL Server"
    TRUST_SERVER_CERTIFICATE: bool = True
    ENCRYPT: str = "yes"
    CONNECTION_TIMEOUT: int = 30
    AUTHENTICATION: str = "SqlPassword"  # SqlPassword, Windows, ActiveDirectoryPassword, etc.

class PostgresSettings(BaseSettings):
    USER: str = "postgres"
    PASSWORD: str = "postgres"
    HOST: str = "localhost"
    PORT: int = 5432
    DATABASE: str = "sage_iq"

class Settings(BaseSettings):
    # PostgreSQL settings
    POSTGRES: PostgresSettings = PostgresSettings()
    
    # SQL Server settings
    SQLSERVER: SQLServerSettings = SQLServerSettings()
    
    # GitHub settings
    GITHUB_TOKEN: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()