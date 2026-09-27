from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    min_stock: int
    category: str

class Product(ProductCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
