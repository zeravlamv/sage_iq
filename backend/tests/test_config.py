import pytest
from backend.models.data.database_config import DatabaseConfig, PostgresConfig, SQLServerConfig
from backend.services.admin.config_service import ConfigService

@pytest.fixture
def valid_config():
    return DatabaseConfig(
        postgres=PostgresConfig(
            host="localhost",
            port=5432,
            database="sage_iq",
            user="postgres",
            password="postgres"
        ),
        sqlserver=SQLServerConfig(
            host="localhost",
            port=1433,
            database="sage_iq",
            user="sa",
            password="StrongPass123!",
            driver="ODBC Driver 17 for SQL Server",
            trust_server_certificate=True,
            encrypt="yes",
            connection_timeout=30,
            authentication="SqlPassword"
        )
    )

@pytest.mark.asyncio
async def test_postgres_config_validation():
    config = PostgresConfig(
        host="localhost",
        port=5432,
        database="sage_iq",
        user="postgres",
        password="postgres"
    )
    assert config.host == "localhost"
    assert config.port == 5432
    assert config.database == "sage_iq"

@pytest.mark.asyncio
async def test_sqlserver_config_validation():
    config = SQLServerConfig(
        host="localhost",
        port=1433,
        database="sage_iq",
        user="sa",
        password="StrongPass123!"
    )
    assert config.host == "localhost"
    assert config.port == 1433
    assert config.database == "sage_iq"
    assert config.driver == "ODBC Driver 17 for SQL Server"  # valor por defecto
    assert config.trust_server_certificate == True  # valor por defecto

@pytest.mark.asyncio
async def test_config_service(valid_config):
    service = ConfigService()
    # Test conexión PostgreSQL
    result = await service.test_postgres_connection(valid_config.postgres)
    assert isinstance(result, bool)

    # Test conexión SQL Server
    result = await service.test_sqlserver_connection(valid_config.sqlserver)
    assert isinstance(result, bool)