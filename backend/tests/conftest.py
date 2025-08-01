import pytest
import os
import sys

# Agregar el directorio raíz al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def test_config():
    return {
        "postgres": {
            "host": "localhost",
            "port": 5432,
            "database": "sage_iq_test",
            "user": "postgres",
            "password": "postgres"
        },
        "sqlserver": {
            "host": "localhost",
            "port": 1433,
            "database": "sage_iq_test",
            "user": "sa",
            "password": "YourStrong!Passw0rd",
            "driver": "ODBC Driver 17 for SQL Server",
            "trust_server_certificate": True,
            "encrypt": "yes",
            "connection_timeout": 30,
            "authentication": "SqlPassword"
        }
    }