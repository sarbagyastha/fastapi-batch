# FastAPI Batch

FastAPI Batch is a Python library that allows you to batch multiple requests into a single request. It is built on top of FastAPI and Pydantic.

```json
{
  "requests": {
    "fruit": {
      "body": {
        "name": "Mango",
        "poisonous": false
      },
      "headers": {
        "content-type": "application/json"
      },
      "method": "POST",
      "url": "/api/v1/fruit"
    },
    "animal": {
      "body": {
        "name": "Lion",
        "carnivore": true
      },
      "headers": {
        "content-type": "application/json"
      },
      "method": "POST",
      "url": "/api/v1/animal"
    }
  }
}
```