# SAGE IQ

Sistema de Análisis y Gestión Empresarial con Inteligencia Artificial.

## Estado del Proyecto
🚀 **Fase 1: Configuración del Entorno** ✅
- [Ver estado detallado del proyecto](./ESTADO_PROYECTO.md)

## Requisitos

### Python
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Bases de Datos
- PostgreSQL 12 o superior
- SQL Server 2019 o superior
- Driver ODBC 17 para SQL Server

## Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone https://github.com/zeravlamv/sage_iq.git
cd sage_iq
```

2. Crear entorno virtual:
```bash
python -m venv venv
```

3. Activar entorno virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

## Estructura del Proyecto

```
backend/
├── routers/                    # Endpoints API
│   └── admin/                  # Endpoints Administrativos
│       └── config.py          # Configuración sistema
├── services/                   # Lógica de Negocio
│   └── admin/                 # Servicios Administrativos
│       └── config_service.py  # Servicio de configuración
├── models/                    # Modelos de Datos
│   └── data/                 # Modelos de Datos
│       ├── database_config.py # Configuración DB
│       └── semantic.py       # Modelos semánticos
├── core/                     # Núcleo Aplicación
│   └── database.py          # Conexiones DB
└── tests/                   # Tests
    ├── test_config.py      # Tests de configuración
    └── test_semantic_models.py # Tests de modelos
```

## Configuración de Bases de Datos

### PostgreSQL (Metadatos)
1. Crear base de datos:
```sql
CREATE DATABASE sage_iq;
```

2. Configurar en `.env`:
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=sage_iq
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### SQL Server (Datos Empresariales)
1. Configurar en `.env`:
```env
SQLSERVER_USER=your_user
SQLSERVER_PASSWORD=your_password
SQLSERVER_DB=sage_iq
SQLSERVER_HOST=your_server
SQLSERVER_PORT=1433
SQLSERVER_DRIVER="ODBC Driver 17 for SQL Server"
SQLSERVER_TRUST_SERVER_CERTIFICATE=true
SQLSERVER_ENCRYPT=yes
SQLSERVER_CONNECTION_TIMEOUT=30
SQLSERVER_AUTHENTICATION=SqlPassword
```

## Desarrollo

### Tests
Ejecutar tests:
```bash
pytest backend/tests/ -v
```

Ejecutar tests con cobertura:
```bash
pytest backend/tests/ -v --cov=backend --cov-report=term-missing
```

### Migraciones
Crear nueva migración:
```bash
alembic revision --autogenerate -m "descripción"
```

Aplicar migraciones:
```bash
alembic upgrade head
```

## Documentación
- [Estado del Proyecto](./ESTADO_PROYECTO.md)
- [Especificación Completa](./PROMPT_PROYECTO_SAGE_IQ_2025.md)

## Contribuir
1. Crear una rama para tu feature: `git checkout -b feature/nombre-feature`
2. Hacer commit de tus cambios: `git commit -am 'feat: Descripción del cambio'`
3. Push a la rama: `git push origin feature/nombre-feature`
4. Crear un Pull Request

## Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.