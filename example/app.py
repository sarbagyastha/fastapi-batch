from fastapi import FastAPI

from example.models import AnimalModel, FruitModel
from fastapi_batch import BatchGateway, BatchResponse


app = FastAPI()


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


@app.post("/api/v1/batch", response_model_exclude_defaults=True)
async def batch_endpoint(gateway: BatchGateway) -> BatchResponse:
    return await gateway.execute()
