# FastAPI Batch 🌟

FastAPI Batch is a Python library that simplifies batching multiple API requests into a single request. Built on top of FastAPI and Pydantic, it empowers developers to optimize API interactions while maintaining flexibility and performance.

## Motivation 💡

In modern web development, making multiple independent API requests can lead to higher overhead, increased latency, and slower overall performance. **FastAPI Batch** was created to address these issues by enabling developers to group multiple requests into a single batch request. This reduces the number of round trips between the client and server, optimizing performance by executing requests in parallel, and improving the user experience.


## Installation 🚀

You can install FastAPI Batch using one of the following methods:

#### Using UV

```bash
uv add fastapi-batch
```

#### Using Poetry

```bash
poetry add fastapi-batch
```

#### Using Pip

```bash
pip install fastapi-batch
```


## Features ✨
- **Batch API Requests** 📦: Combine multiple API calls into a single request to reduce overhead.  
- **Parallel Request Execution** ⚡: Automatically execute batched requests in parallel for better performance.  
- **Customizable Headers** 📝: Override or define custom headers for individual requests in a batch.  
- **Lightweight & Flexible** 🪶: Easily integrates with existing FastAPI applications.  
- **Seamless Response Handling** 💨: Structured responses for each request in the batch.  


## Quick Start 🛠

Here’s how to set up FastAPI Batch in your project:

### Example Usage

Define your API endpoints:

```python
from fastapi_batch import BatchGateway, BatchResponse

@app.post("/api/v1/fruit")
async def identify_fruit(fruit: FruitModel):
    return {
        "message": f"{fruit.name} is a fruit and is{' ' if fruit.poisonous else ' not '}poisonous."
    }

@app.post("/api/v1/animal")
async def identify_animal(animal: AnimalModel):
    return {
        "message": f"{animal.name} is an animal and is{' ' if animal.carnivore else ' not '}a carnivorous."
    }

@app.post("/api/v1/batch")
async def batch_endpoint(gateway: BatchGateway) -> BatchResponse:
    return await gateway.execute()
```


#### Sample Batch Request

Send multiple requests to the /api/v1/batch endpoint in a single payload. You can override headers or customize them for individual requests:

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
      "headers": {
        "content-type": "application/json"
      },
      "method": "POST",
      "url": "/api/v1/animal"
    }
  }
}
```

#### Batch Response

Receive individual responses for all requests in a structured format:

```json
{
  "responses": {
    "fruit": {
      "body": {
        "message": "Mango is a fruit and is not poisonous."
      },
      "status_code": 200
    },
    "animal": {
      "body": {
        "message": "Lion is an animal and is a carnivorous."
      },
      "status_code": 200
    }
  }
}
```


## 📖 Full Example

Explore the [example directory](https://github.com/sarbagyastha/fastapi-batch/tree/main/example) for a complete demonstration of FastAPI Batch in action.


## Contributions 🤝
We welcome contributions to enhance FastAPI Batch! Feel free to:
- Open issues and feature requests.
- Submit pull requests with your improvements.

Let’s build something amazing together! 🎉


## License 📜
FastAPI Batch is open source and available under the [MIT License](https://github.com/sarbagyastha/fastapi-batch/blob/main/LICENSE.md).

---

Enjoy faster, cleaner, and more efficient API interactions with FastAPI Batch! 🐍🚀
