# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from typing import Annotated
from fastapi_batch.models import (
    BatchRequest,
    RequestBatchModel,
    ResponseBatchModel,
)
from fastapi import Depends, Request
from httpx import AsyncClient
from asyncer import SoonValue, create_task_group

from fastapi_batch.models.batch_response import BatchResponse


class _BatchGateway:
    async def __call__(self, batch: BatchRequest, request: Request) -> "_BatchGateway":
        self.host = f"{request.url.scheme}://{request.url.netloc}"
        self.__headers = request.headers
        self.__requests = batch.requests
        self.__include_response_headers = batch.include_response_headers
        return self

    async def execute(self) -> BatchResponse:
        """Executes the batch of requests."""

        async with AsyncClient() as client:
            soon_values: dict[str, SoonValue] = {}
            async with create_task_group() as tg:
                for id, batch_request in self.__requests.items():
                    soon_values[id] = tg.soonify(self.__request)(
                        client, self.__include_response_headers, batch_request
                    )

            return BatchResponse(
                responses={
                    id: soon_value.value for id, soon_value in soon_values.items()
                }
            )

    async def __request(
        self,
        client: AsyncClient,
        include_response_headers: bool,
        request: RequestBatchModel,
    ) -> ResponseBatchModel:
        request_headers: dict[str, str] = {
            **self.__headers,
            **(request.headers or {}),
        }
        request_headers.pop("content-length")

        response = await client.request(
            url=f"{self.host}{request.url}",
            method=request.method,
            headers=request_headers,
            json=request.body,
        )

        response_headers = (
            {k: v for k, v in response.headers.items()}
            if include_response_headers
            else None
        )

        return ResponseBatchModel(
            headers=response_headers,
            body=response.json(),
            status_code=response.status_code,
        )


BatchGateway = Annotated[_BatchGateway, Depends(_BatchGateway())]
"""FastAPI dependency for executing multiple requests in a batch."""
