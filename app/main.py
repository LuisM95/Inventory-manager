from fastapi import FastAPI 
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

from app.routes.product import router as products_router

import time 

app = FastAPI(
        title="DevOps Inventory Manager",
        description="Production-ready Inventory Management",
        version="1.0.0"
        )

REQUEST_COUNT = Counter (
        'http_request_total',
        'Total HTTP request',
        ['method', 'endpoint', 'status']
        )

# Routers
app.include_router(products_router)


@app.get('/')
async def root():
    return {
            "service":"DevOps Inventory Manager",
            "version":"1.0.0",
            "status": "running"
            }

@app.get('/health')
async def health():
    return {
            "status":"healthy",
            "database":"connected",
            "cache":"connected"
            }
@app.get('/metrics')
async def metrics():
    return Response(
            generate_latest(),
            media_type=CONTENT_TYPE_LATEST
    )


