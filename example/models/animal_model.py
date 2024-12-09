from pydantic import BaseModel


class AnimalModel(BaseModel):
    name: str
    carnivore: bool
