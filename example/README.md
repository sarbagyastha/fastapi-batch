# FastAPI Batch Example 🍇🍖

## Try It Out 🚀

To get started with the example, follow these steps:

```bash
uv sync                     # Sync the environment
source .venv/bin/activate   # Activate your virtual environment
fastapi dev                 # Start the FastAPI server in development mode
```

Once the server is running, navigate to http://localhost:8000/docs to interact with the API via Swagger UI. 🌐

> [!NOTE] Note 📝
Don’t forget to include the `Authorization: Bearer batch-token` header for authentication.


#### Sample Request 📬

Here’s an example of a batched request you can send to the /api/v1/batch endpoint:

```json
{
  "requests": {
    "fruit": {
      "body": {
        "name": "Mango",
        "poisonous": false
      },
      "method": "POST",
      "url": "/api/v1/fruit"
    },
    "animal": {
      "body": {
        "name": "Lion",
        "carnivore": true
      },
      "method": "POST",
      "url": "/api/v1/animal"
    }
  }
}
```

This batch will send two requests: one to identify the fruit and another to identify the animal. 🥭🦁