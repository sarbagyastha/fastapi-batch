from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer

from models import AnimalModel, FruitModel
from fastapi_batch import BatchGateway, BatchResponse


class BatchBearer(HTTPBearer):
    async def __call__(self, request: Request) -> None:
        if request.headers.get("Authorization") != "Bearer batch-token":
            raise ValueError("You're not authorized to access this resource.")


app = FastAPI(dependencies=[Depends(BatchBearer())])


@app.exception_handler(ValueError)
async def validation_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=418,
        content={"message": exc.args[0]},
    )


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
