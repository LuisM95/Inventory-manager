# Devops Inventory Manager

Production-ready Inventory Manager API build with DevOps best practices.

## Tech Stack 
- **Backend**: FastApi (Python)
- **Database:** PostgreSQL
- **Cache:** Redis
- **Container:** Docker + Docker compose
- **Registry:** AWS ECR
- **Deploy:** AWS ECS
- **IaC:** Terraform 
- **CI/CD:** Github Actions
- **Monitoring:** Prometheus + Grafana

## Architecture.

Github -> Github Actions -> AWS ECR -> AWS ECS  -> Production
↓
Test + Build + Push + Deploy

## API Endpoints.
|    Method    |       EndPoint        |       Description       |
|--------------|-----------------------|-------------------------|
|     GET      |      /products        |    List all products    |
|     GET      |    /products/{id}     |   Get product by ID     |
|     POST     |      /products        |     Create product      |
|     PUT      |    /products/{id}     |     Update product      |
|    DELETE    |    /products/{id}     |     Delete product      |
|     GET      |   /product/low-stock  |  Products with low stock|
|     POST     |/products/{id}/movement| Register stock movement |
|     GET      |        /health        |       Health check      |
|     GET      |        /metrics       |    Prometheus Metrics   |

## Status 
🚧 In Development
