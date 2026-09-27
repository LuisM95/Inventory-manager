from fastapi import FastAPI 
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.response import Response
import time 

app = FastAPI(
        title="DevOps Inventory Manager",
        description="Production-ready Inventory Management"
        version="1.0.0"
        )

REQUEST_COUNT = Counter (
        'http_request_total',
        'Total HTTP request',
        ['method', 'endpoint', 'status']
        )


@app.get('/')
async def root():
    return {
            "service":"DevOps Intenvory Manager",
            "version":"1.0.0",
            "status": "running"
            }

@app.get('/health')
async def health():
    return {
            "status":"healtly",
            "database":"connected",
            "cache":"connected"
            }
@app.get('/metrics')
async def metrics():
    return Response(
            genetate_latest(),
            media_type=CONTENT_TYPE_LATEST
    )


