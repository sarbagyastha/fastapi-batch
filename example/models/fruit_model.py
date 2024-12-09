from pydantic import BaseModel


class FruitModel(BaseModel):
    name: str
    poisonous: bool
