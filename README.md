# FastAPI Batch

FastAPI Batch is a Python library that allows you to batch multiple requests into a single request. It is built on top of FastAPI and Pydantic.


## Installation

```bash
uv add fastapi-batch
```


## Usage

```python
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

#### Request
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

### Response
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

## License
Copyright 2024 Sarbagya Dhaubanjar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.