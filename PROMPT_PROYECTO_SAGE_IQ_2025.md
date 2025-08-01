# 🎯 PROMPT PARA RECREACIÓN DE SAGE.IQ (2025)

## Visión General del Proyecto

SAGE.IQ es una plataforma de análisis inteligente que transforma datos empresariales de SAGE 200 en insights accionables mediante IA y procesamiento de lenguaje natural. El sistema permite realizar consultas en lenguaje natural sobre datos empresariales con máxima seguridad y control.

## 🏗️ Arquitectura del Sistema

### Componentes Principales

1. **Backend (FastAPI + Python)**
   - API REST con autenticación JWT
   - Middleware de seguridad
   - Servicios modulares
   - PostgreSQL para metadatos semánticos
   - SQL Server para datos empresariales SAGE 200

2. **Frontend Dual (Streamlit)**
   - Interfaz Administrativa (Puerto 8503)
     - Gestión de usuarios y permisos
     - Configuración de reglas de negocio
     - Monitoreo y métricas
     - Gestión de metadatos semánticos
   - Interfaz Cliente (Puerto 8504)
     - Sistema de consultas en lenguaje natural
     - Procesamiento de lenguaje natural
     - Análisis semántico empresarial
     - Generación y optimización de SQL
     - Visualización con Plotly

3. **Motor de IA**
   - Ollama con modelo llama3.1:8b
   - Vectorización y embeddings
   - Indexación semántica
   - Soporte al procesamiento de consultas

4. **Base de Datos Dual**
   - PostgreSQL: Metadatos semánticos y configuración
   - SQL Server: Datos empresariales SAGE 200

### Estructura del Backend

```python
# Estructura de Directorios Backend
SAGE.IQ/
├── backend/
│   ├── routers/                    # Endpoints API
│   │   ├── auth/                   # Autenticación y Autorización
│   │   │   ├── jwt.py             # Gestión de tokens JWT
│   │   │   ├── roles.py           # Control de roles
│   │   │   └── permissions.py      # Gestión de permisos
│   │   ├── admin/                  # Endpoints Administrativos
│   │   │   ├── users.py           # Gestión de usuarios
│   │   │   ├── config.py          # Configuración sistema
│   │   │   ├── audit.py           # Logs y auditoría
│   │   │   └── metrics.py         # Métricas y monitoreo
│   │   ├── data/                  # Endpoints de Datos
│   │   │   ├── tables.py          # Gestión de tablas
│   │   │   ├── fields.py          # Gestión de campos
│   │   │   ├── relationships.py    # Relaciones entre tablas
│   │   │   └── metadata.py        # Metadatos semánticos
│   │   └── integration/           # Integraciones
│   │       ├── sage200.py         # Conexión SAGE 200
│   │       ├── ollama.py          # Integración Ollama
│   │       └── export.py          # Exportación datos
│   ├── services/                  # Lógica de Negocio
│   │   ├── admin/                 # Servicios Administrativos
│   │   │   ├── user_service.py    # Gestión usuarios
│   │   │   ├── audit_service.py   # Auditoría
│   │   │   └── metric_service.py  # Métricas
│   │   ├── data/                  # Servicios de Datos
│   │   │   ├── table_service.py   # Operaciones tablas
│   │   │   ├── field_service.py   # Operaciones campos
│   │   │   └── query_service.py   # Procesamiento consultas
│   │   ├── security/              # Servicios Seguridad
│   │   │   ├── auth_service.py    # Autenticación
│   │   │   ├── role_service.py    # Roles
│   │   │   └── audit_log.py       # Logging seguridad
│   │   └── integration/           # Servicios Integración
│   │       ├── sage_service.py    # Lógica SAGE 200
│   │       └── ollama_service.py  # Lógica Ollama
│   ├── models/                    # Modelos de Datos
│   │   ├── auth/                  # Modelos Autenticación
│   │   │   ├── user.py           # Usuario
│   │   │   ├── role.py           # Roles
│   │   │   └── permission.py     # Permisos
│   │   ├── data/                 # Modelos Datos
│   │   │   ├── table.py          # Tablas
│   │   │   ├── field.py          # Campos
│   │   │   └── relationship.py   # Relaciones
│   │   └── audit/                # Modelos Auditoría
│   │       ├── log.py            # Logs
│   │       └── metric.py         # Métricas
│   ├── core/                     # Núcleo Aplicación
│   │   ├── config.py            # Configuración
│   │   ├── security.py          # Seguridad
│   │   ├── database.py          # Conexiones DB
│   │   └── constants.py         # Constantes
│   ├── middleware/              # Middleware
│   │   ├── auth.py             # Autenticación
│   │   ├── audit.py            # Auditoría
│   │   └── error.py            # Manejo errores
│   └── utils/                  # Utilidades
       ├── validators.py        # Validadores
       ├── formatters.py        # Formateadores
       └── helpers.py          # Funciones auxiliares
```

### Endpoints API Backend

#### 1. Autenticación y Autorización
```python
# auth/jwt.py
@router.post("/auth/login")
async def login(credentials: LoginCredentials) -> Token

@router.post("/auth/refresh")
async def refresh_token(token: Token) -> Token

@router.post("/auth/logout")
async def logout(token: Token) -> Response

# auth/roles.py
@router.get("/roles")
async def get_roles() -> List[Role]

@router.post("/roles")
async def create_role(role: RoleCreate) -> Role

@router.put("/roles/{role_id}")
async def update_role(role_id: int, role: RoleUpdate) -> Role
```

#### 2. Gestión de Usuarios
```python
# admin/users.py
@router.get("/users")
async def get_users(filters: UserFilters) -> List[User]

@router.post("/users")
async def create_user(user: UserCreate) -> User

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate) -> User

@router.delete("/users/{user_id}")
async def delete_user(user_id: int) -> Response
```

#### 3. Configuración y Metadatos
```python
# admin/config.py
@router.get("/config")
async def get_config() -> SystemConfig

@router.put("/config")
async def update_config(config: SystemConfigUpdate) -> SystemConfig

# data/metadata.py
@router.get("/metadata/tables")
async def get_tables_metadata() -> List[TableMetadata]

@router.get("/metadata/fields/{table_id}")
async def get_fields_metadata(table_id: int) -> List[FieldMetadata]
```

#### 4. Gestión de Datos
```python
# data/tables.py
@router.get("/tables")
async def get_tables(filters: TableFilters) -> List[Table]

@router.get("/tables/{table_id}/schema")
async def get_table_schema(table_id: int) -> TableSchema

# data/relationships.py
@router.get("/relationships")
async def get_relationships(table_id: Optional[int] = None) -> List[Relationship]

@router.post("/relationships")
async def create_relationship(relationship: RelationshipCreate) -> Relationship
```

#### 5. Auditoría y Métricas
```python
# admin/audit.py
@router.get("/audit/logs")
async def get_audit_logs(filters: AuditLogFilters) -> List[AuditLog]

@router.get("/audit/actions/{user_id}")
async def get_user_actions(user_id: int) -> List[UserAction]

# admin/metrics.py
@router.get("/metrics/system")
async def get_system_metrics() -> SystemMetrics

@router.get("/metrics/usage")
async def get_usage_metrics() -> UsageMetrics
```

### Servicios Backend

#### 1. Servicio de Autenticación
```python
# services/security/auth_service.py
class AuthenticationService:
    async def authenticate_user(self, credentials: LoginCredentials) -> User:
        """Autenticación de usuario contra AD/LDAP"""
        pass

    async def create_access_token(self, user: User) -> Token:
        """Generación de token JWT"""
        pass

    async def validate_token(self, token: str) -> TokenData:
        """Validación de token JWT"""
        pass
```

#### 2. Servicio de Datos
```python
# services/data/query_service.py
class QueryService:
    async def execute_query(self, query: str, params: Dict) -> QueryResult:
        """Ejecuta consulta validada"""
        pass

    async def validate_query(self, query: str) -> bool:
        """Validación de seguridad de consulta"""
        pass

    async def optimize_query(self, query: str) -> str:
        """Optimización de consulta"""
        pass
```

#### 3. Servicio de Auditoría
```python
# services/admin/audit_service.py
class AuditService:
    async def log_action(self, user: User, action: str, details: Dict):
        """Registro de acciones de usuario"""
        pass

    async def get_user_activity(self, user_id: int) -> List[Activity]:
        """Obtiene actividad de usuario"""
        pass

    async def generate_audit_report(self, filters: AuditFilters) -> Report:
        """Genera reporte de auditoría"""
        pass
```

### Modelos de Datos Backend

#### 1. Modelos de Usuario
```python
# models/auth/user.py
class User(BaseModel):
    id: int
    username: str
    email: str
    role_id: int
    is_active: bool
    last_login: datetime
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role_id: int

class UserUpdate(BaseModel):
    email: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool]
```

#### 2. Modelos de Datos
```python
# models/data/table.py
class Table(BaseModel):
    id: int
    name: str
    display_name: str
    schema: str
    description: str
    is_visible: bool
    metadata: Dict

class Field(BaseModel):
    id: int
    table_id: int
    name: str
    data_type: str
    is_nullable: bool
    description: str
    semantic_type: str
```

#### 3. Modelos de Auditoría
```python
# models/audit/log.py
class AuditLog(BaseModel):
    id: int
    user_id: int
    action: str
    entity_type: str
    entity_id: int
    details: Dict
    ip_address: str
    timestamp: datetime

class Metric(BaseModel):
    id: int
    metric_type: str
    value: float
    timestamp: datetime
    metadata: Dict
```
├── frontend_admin/         # Interfaz administrativa
│   ├── pages/             # Páginas de administración
│   │   ├── users.py       # Gestión de usuarios
│   │   ├── config.py      # Configuración
│   │   └── metrics.py     # Monitoreo
│   └── components/        # Componentes reutilizables
├── frontend_cliente/       # Interfaz usuario final
│   ├── pages/             # Páginas de cliente
│   │   ├── query.py       # Consultas naturales
│   │   ├── results.py     # Visualización
│   │   └── history.py     # Historial
│   ├── nlp/               # Procesamiento lenguaje natural
│   │   ├── processor.py   # Procesador principal
│   │   ├── analyzer.py    # Análisis semántico
│   │   └── generator.py   # Generación SQL
│   └── components/        # Componentes visuales
└── docs/                  # Documentación
```

[... Resto del contenido del prompt se mantiene igual hasta la sección de Análisis de Consultas Empresariales ...]

### 3. Análisis de Consultas Empresariales (Frontend Cliente)

#### Procesamiento de Lenguaje Natural
```python
class NaturalLanguageProcessor:
    """
    Procesador integrado en frontend cliente:
    1. Análisis de consulta natural
    2. Extracción de intención
    3. Identificación de entidades
    4. Contextualización empresarial
    """
    async def process_query(self, query: str) -> Dict:
        return {
            "intent": self.extract_intent(query),
            "entities": self.identify_entities(query),
            "context": self.get_business_context(query),
            "parameters": self.extract_parameters(query)
        }

    async def generate_sql(self, processed_query: Dict) -> str:
        """Genera SQL basado en el análisis de la consulta"""
        pass

    async def validate_query(self, sql: str) -> bool:
        """Valida la consulta SQL generada"""
        pass
```

[... Continúa el resto del prompt con las secciones actualizadas ...]