from sqlalchemy.orm import Session 
from app.database.models import Product 
from app.models.product import ProductCreate

# Method for get all products 
def get_all_products(db: Session):
    return db.query(Product).all()

#Method for find a product by id 
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id:int, product:ProductCreate):
    db_product = get_product_by_id(db, product_id)
    if db_product is None:
        return None
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id:int):
    db_product = get_product_by_id(db, product_id)
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product

def get_low_stock_products(db: Session):
    return db.query(Product).filter(Product.stock <= Product.min_stock).all()


