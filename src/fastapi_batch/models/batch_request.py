# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, Field, field_validator

from fastapi_batch.models.batch_model import Keyed, RequestBatchModel


class BatchRequest(BaseModel):
    include_response_headers: bool = False
    requests: Annotated[Keyed[RequestBatchModel], MaxLen(15), MinLen(1)] = Field(
        examples=[
            {
                "id": {
                    "headers": {
                        "content-type": "application/json",
                    },
                    "body": {"message": "Hello, World!"},
                    "url": "/api/v1/example",
                    "method": "POST",
                }
            }
        ]
    )

    @field_validator("requests")
    @classmethod
    def ensure_requests_are_unique(
        cls, v: dict[str, RequestBatchModel]
    ) -> dict[str, RequestBatchModel]:
        visited_ids = set()
        for id in v.keys():
            if id in visited_ids:
                raise ValueError(
                    f"Batch request ids must be unique, found duplicate id: {id}"
                )
            visited_ids.add(id)
        return v
