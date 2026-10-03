from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['service'] == "DevOps Inventory Manager"

def test_create_product():
    response = client.post("/products/" , json={
        "name":"Test product",
        "description":"Test description",
        "price":99.99,
        "stock":100,
        "min_stock":10,
        "category":"Test"
    })
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == "Test product"
    assert data['price'] == 99.99
    assert "id" in data

def test_get_products():
    response = client.get('/products/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product_not_found():
    response = client.get('/products/99999')
    assert response.status_code == 404

def test_low_stock():
    #create a product with low stock
    client.post('/products/' , json={
        "name":"Low Stock Product",
        "description":"Test",
        "price":10.00,
        "stock":5,
        "min_stock":10,
        "category": "Test"
    })
    response = client.get('/products/low-stock')
    assert response.status_code == 200
    assert len(response.json()) > 0
        
        
