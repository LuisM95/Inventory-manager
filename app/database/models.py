from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()  # clase base para todos los modelos

class Product(Base):
    __tablename__ = "products"  # nombre de la tabla en PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # autoincremental
    name = Column(String, nullable=False)               # obligatorio
    description = Column(String, nullable=True)         # opcional
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    min_stock = Column(Integer, default=10)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
