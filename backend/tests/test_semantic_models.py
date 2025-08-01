import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from backend.models.data.semantic import Base, SemanticTable, SemanticField, TableRelationship

@pytest.fixture
def test_db():
    # Crear base de datos en memoria para testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)
    yield session
    session.close()

def test_create_semantic_table(test_db):
    table = SemanticTable(
        table_name="customers",
        display_name="Clientes",
        description="Tabla de clientes",
        module="sales"
    )
    test_db.add(table)
    test_db.commit()
    
    assert table.id is not None
    assert table.table_name == "customers"
    assert table.is_active == True

def test_create_semantic_field(test_db):
    # Crear tabla primero
    table = SemanticTable(
        table_name="customers",
        display_name="Clientes"
    )
    test_db.add(table)
    test_db.commit()

    # Crear campo
    field = SemanticField(
        table_id=table.id,
        field_name="customer_id",
        display_name="ID Cliente",
        data_type="integer",
        is_primary_key=True
    )
    test_db.add(field)
    test_db.commit()

    assert field.id is not None
    assert field.table_id == table.id
    assert field.is_primary_key == True

def test_create_table_relationship(test_db):
    # Crear tablas
    customers = SemanticTable(table_name="customers", display_name="Clientes")
    orders = SemanticTable(table_name="orders", display_name="Pedidos")
    test_db.add_all([customers, orders])
    test_db.commit()

    # Crear relación
    relationship = TableRelationship(
        source_table_id=customers.id,
        target_table_id=orders.id,
        source_field="customer_id",
        target_field="customer_id",
        relationship_type="one_to_many",
        confidence=100
    )
    test_db.add(relationship)
    test_db.commit()

    assert relationship.id is not None
    assert relationship.source_table_id == customers.id
    assert relationship.target_table_id == orders.id