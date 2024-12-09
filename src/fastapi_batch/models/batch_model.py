# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from typing import Any
from urllib.parse import urlparse
from pydantic import BaseModel, field_validator
from fastapi_batch.models.http_methods import HTTPMethods

type Keyed[T] = dict[str, T]


class BatchModel(BaseModel):
    headers: dict[str, str] | None = None
    body: Any | None


class RequestBatchModel(BatchModel):
    url: str
    method: HTTPMethods

    @field_validator("url")
    @classmethod
    def url_is_relative(cls, v: str) -> str:
        if bool(urlparse(v).netloc):
            raise ValueError(
                "Invalid URL: Absolute URLs (e.g., 'http://example.com') are not allowed. "
                "Please provide a relative URL."
            )
        if not v.startswith("/"):
            raise ValueError(
                "Invalid URL: Relative URLs must start with a leading '/'. "
                "For example, '/path/to/resource'."
            )
        return v


class ResponseBatchModel(BatchModel):
    status_code: int
