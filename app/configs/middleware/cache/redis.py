#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: redis
Time: 2025/6/27 17:24
"""
from typing import Optional

from pydantic import Field, PositiveInt, NonNegativeInt
from pydantic_settings import BaseSettings


class RedisConfig(BaseSettings):
    REDIS_HOST: str = Field(
        description="Hostname or IP address of the Redis server",
        default="localhost",
    )

    REDIS_PORT: PositiveInt = Field(
        description="Port number on which the Redis server is listening",
        default=6379,
    )

    REDIS_USERNAME: Optional[str] = Field(
        description="Username for Redis authentication (if required)",
        default=None,
    )

    REDIS_PASSWORD: Optional[str] = Field(
        description="Password for Redis authentication (if required)",
        default=None,
    )

    REDIS_DB: NonNegativeInt = Field(
        description="Redis database number to use (0-15)",
        default=0,
    )
