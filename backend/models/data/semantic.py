from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.core.database import Base

class SemanticTable(Base):
    __tablename__ = "semantic_tables"

    id = Column(Integer, primary_key=True, index=True)
    table_name = Column(String(100), nullable=False)
    display_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    context = Column(Text, nullable=True)
    module = Column(String(50), nullable=True)
    row_count = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    fields = relationship("SemanticField", back_populates="table")

class SemanticField(Base):
    __tablename__ = "semantic_fields"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("semantic_tables.id"))
    field_name = Column(String(100), nullable=False)
    display_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    data_type = Column(String(50), nullable=False)
    is_nullable = Column(Boolean, nullable=True)
    max_length = Column(Integer, nullable=True)
    is_primary_key = Column(Boolean, nullable=True)
    is_foreign_key = Column(Boolean, nullable=True)
    semantic_type = Column(String(50), nullable=True)
    examples = Column(JSON, nullable=True)
    patterns = Column(JSON, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    table = relationship("SemanticTable", back_populates="fields")

class TableRelationship(Base):
    __tablename__ = "table_relationships"

    id = Column(Integer, primary_key=True, index=True)
    source_table_id = Column(Integer, ForeignKey("semantic_tables.id"))
    target_table_id = Column(Integer, ForeignKey("semantic_tables.id"))
    source_field = Column(String(100), nullable=False)
    target_field = Column(String(100), nullable=False)
    relationship_type = Column(String(20), nullable=True)
    confidence = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())