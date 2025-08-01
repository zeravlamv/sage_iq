from setuptools import setup, find_packages

setup(
    name="sage_iq",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "alembic",
        "psycopg2-binary",
        "pyodbc",
        "uvicorn",
        "python-dotenv",
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "httpx"
    ],
)