# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from pydantic import BaseModel

from fastapi_batch.models.batch_model import Keyed, ResponseBatchModel


class BatchResponse(BaseModel):
    responses: Keyed[ResponseBatchModel]
