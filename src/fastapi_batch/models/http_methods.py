# Copyright (c) 2024 Sarbagya Dhaubanjar
# Licensed under the MIT License. See LICENSE file for details.

from enum import StrEnum


class HTTPMethods(StrEnum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"
