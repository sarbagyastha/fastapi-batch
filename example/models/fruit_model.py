# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from pydantic import BaseModel


class FruitModel(BaseModel):
    name: str
    poisonous: bool
