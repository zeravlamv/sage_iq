from pydantic import BaseModel
from typing import Optional

class PostgresConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str
    
class SQLServerConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str
    driver: str = "ODBC Driver 17 for SQL Server"
    trust_server_certificate: bool = True
    encrypt: str = "yes"
    connection_timeout: int = 30
    authentication: str = "SqlPassword"

class DatabaseConfig(BaseModel):
    postgres: PostgresConfig
    sqlserver: SQLServerConfig