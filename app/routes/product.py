from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.product import Product, ProductCreate
from app.services.product_service import (
        get_all_products,
        get_product_by_id,
        create_product,
        update_product,
        delete_product,
        get_low_stock_products
)


router = APIRouter(
        prefix = '/products',
        tags=['products'],
        responses={404: {'Message':'Not Found'}}
        )

@router.get('/')
async def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.get('/low-stock')
async def low_stock(db: Session = Depends(get_db)):
    return get_low_stock_products(db)

@router.get('/{product_id}')
async def get_product(product_id:int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    return product

@router.post('/')
async def add_product(product:ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.put('/{product_id}')
async def modify_product(product_id:int, product:ProductCreate, db: Session = Depends(get_db)):
    updated = update_product(db, product_id, product)
    if updated is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    return updated

@router.delete('/{product_id}')
async def remove_product(product_id:int, db: Session = Depends(get_db)):
    deleted = delete_product(db, product_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Product not found!")
    return {"Message":"Product Deleted Successfully!"}

