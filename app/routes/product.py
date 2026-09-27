from fastapi import APIRouter 

router = APIRouter(
        prefix = '/products',
        tags=['products'],
        responses={404: {'Message':'Not Found'}}
        )

product_list = []

@router.get('/')
async def get_products():
    return product_list

@router.get('/{id}')
async def get_product(id:int):
    return product_list[id]
