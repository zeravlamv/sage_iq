from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from urllib.parse import quote_plus

def get_postgres_url():
    return f"postgresql://{settings.POSTGRES.USER}:{settings.POSTGRES.PASSWORD}@{settings.POSTGRES.HOST}:{settings.POSTGRES.PORT}/{settings.POSTGRES.DATABASE}"

def get_sqlserver_url():
    connection_string = (
        f"DRIVER={{{settings.SQLSERVER.DRIVER}}};"
        f"SERVER={settings.SQLSERVER.HOST};"
        f"DATABASE={settings.SQLSERVER.DATABASE};"
        f"UID={settings.SQLSERVER.USER};"
        f"PWD={settings.SQLSERVER.PASSWORD};"
        f"PORT={settings.SQLSERVER.PORT};"
        f"TrustServerCertificate={str(settings.SQLSERVER.TRUST_SERVER_CERTIFICATE)};"
        f"Encrypt={settings.SQLSERVER.ENCRYPT};"
        f"Authentication={settings.SQLSERVER.AUTHENTICATION};"
        f"ConnectionTimeout={settings.SQLSERVER.CONNECTION_TIMEOUT}"
    )
    return f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"

# PostgreSQL connection
postgres_engine = create_engine(get_postgres_url())
PostgresSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)

# SQL Server connection string (not creating engine yet)
sqlserver_url = get_sqlserver_url()

# Base class for models
Base = declarative_base()

# Dependency to get DB sessions
def get_postgres_db():
    db = PostgresSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create SQL Server engine when needed
def create_sqlserver_engine():
    return create_engine(sqlserver_url)