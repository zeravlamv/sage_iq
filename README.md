# SAGE IQ

Sistema de Análisis y Gestión Empresarial con Inteligencia Artificial.

## Estructura del Proyecto

```
backend/
├── routers/                    # Endpoints API
│   ├── auth/                   # Autenticación y Autorización
│   ├── admin/                  # Endpoints Administrativos
│   ├── data/                   # Endpoints de Datos
│   └── integration/            # Integraciones
├── services/                   # Lógica de Negocio
│   ├── admin/                  # Servicios Administrativos
│   ├── data/                   # Servicios de Datos
│   ├── security/              # Servicios de Seguridad
│   └── integration/           # Servicios de Integración
├── models/                    # Modelos de Datos
│   ├── auth/                  # Modelos de Autenticación
│   ├── data/                  # Modelos de Datos
│   └── audit/                 # Modelos de Auditoría
├── core/                      # Núcleo de la Aplicación
├── middleware/               # Middlewares
└── utils/                    # Utilidades
```

## Configuración del Entorno

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Configuración de Bases de Datos

### PostgreSQL (Metadatos)
- Base de datos para metadatos semánticos y configuración
- Configuración en `.env`:
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=sage_iq
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### SQL Server (Datos Empresariales)
- Base de datos para datos empresariales SAGE 200
- Configuración en `.env`:
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

## Estado del Proyecto

### Fase 1: Configuración del Entorno ✅
- [x] Configuración del Repositorio Git
- [x] Configuración del entorno virtual y dependencias
- [x] Estructura del proyecto según documentación
- [x] Implementar modelos base para metadatos semánticos
- [x] Configurar migraciones con Alembic
- [x] Implementar tests unitarios
- [x] Implementar tests de integración
- [x] Documentación del proyecto

### Próximas Fases
- [ ] Fase 2: Implementación Backend
- [ ] Fase 3: Motor de IA
- [ ] Fase 4: Frontend Dual
- [ ] Fase 5: Testing y Despliegue

## Cobertura de Código
```
Name                                       Stmts   Miss  Cover
------------------------------------------------------------------------
backend/models/__init__.py                     0      0   100%
backend/models/data/__init__.py                0      0   100%
backend/models/data/database_config.py        22      0   100%
backend/models/data/semantic.py               48      0   100%
backend/services/admin/config_service.py      31      5    84%
backend/tests/__init__.py                      0      0   100%
backend/tests/conftest.py                      7      1    86%
backend/tests/test_config.py                  27      0   100%
backend/tests/test_semantic_models.py         39      0   100%
------------------------------------------------------------------------
TOTAL                                        222     38    83%
```