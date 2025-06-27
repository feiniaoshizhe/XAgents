#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: __init__.py
Time: 2025/6/27 17:24
"""
import os
from typing import Any, Optional
from urllib.parse import quote_plus, parse_qsl

from pydantic import Field, PositiveInt, computed_field, NonNegativeInt, PositiveFloat
from pydantic_settings import BaseSettings

from configs.middleware.cache.redis import RedisConfig
from configs.middleware.vector_db.elastic_search import ElasticsearchConfig
from configs.middleware.vector_db.milvus import MilvusConfig


class DatabaseConfig(BaseSettings):
    DB_HOST: str = Field(default="localhost")

    DB_PORT: PositiveInt = Field(default=5432)

    DB_USERNAME: str = Field(default="root")

    DB_PASSWORD: str = Field(default="")

    DB_DATABASE: str = Field(default="fast_rag")

    DB_CHARSET: str = Field(default="")

    DB_EXTRAS: str = Field(default="")

    SQLALCHEMY_DATABASE_URI_SCHEME: str = Field(
        description="Database URI scheme for SQLAlchemy connection.",
        default="postgresql",
    )

    @computed_field
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        db_extras = (
            f"{self.DB_EXTRAS}&client_encoding={self.DB_CHARSET}" if self.DB_CHARSET else self.DB_EXTRAS
        ).strip("&")
        db_extras = f"?{db_extras}" if db_extras else ""
        return (
            f"{self.SQLALCHEMY_DATABASE_URI_SCHEME}://"
            f"{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"
            f"{db_extras}"
        )

    SQLALCHEMY_POOL_SIZE: NonNegativeInt = Field(default=30)

    SQLALCHEMY_MAX_OVERFLOW: NonNegativeInt = Field(default=10)

    SQLALCHEMY_POOL_RECYCLE: NonNegativeInt = Field(default=3600)

    SQLALCHEMY_POOL_PRE_PING: bool = Field(default=False)

    SQLALCHEMY_ECHO: bool | str = Field(default=False)

    RETRIEVAL_SERVICE_EXECUTORS: NonNegativeInt = Field(default=os.cpu_count() or 1)

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_ENGINE_OPTIONS(self) -> dict[str, Any]:
        # Parse DB_EXTRAS for 'options'
        db_extras_dict = dict(parse_qsl(self.DB_EXTRAS))
        options = db_extras_dict.get("options", "")
        # Always include timezone
        timezone_opt = "-c timezone=UTC"
        if options:
            # Merge user options and timezone
            merged_options = f"{options} {timezone_opt}"
        else:
            merged_options = timezone_opt

        connect_args = {"options": merged_options}

        return {
            "pool_size": self.SQLALCHEMY_POOL_SIZE,
            "max_overflow": self.SQLALCHEMY_MAX_OVERFLOW,
            "pool_recycle": self.SQLALCHEMY_POOL_RECYCLE,
            "pool_pre_ping": self.SQLALCHEMY_POOL_PRE_PING,
            "connect_args": connect_args,
        }


class CeleryConfig(DatabaseConfig):
    CELERY_BACKEND: str = Field(default="database")

    CELERY_BROKER_URL: Optional[str] = Field(default=None)

    CELERY_USE_SENTINEL: Optional[bool] = Field(default=False)

    CELERY_SENTINEL_MASTER_NAME: Optional[str] = Field(default="redis-master")

    CELERY_SENTINEL_SOCKET_TIMEOUT: Optional[PositiveFloat] = Field(default=0.1)

    @computed_field
    def CELERY_RESULT_BACKEND(self) -> str | None:
        return (
            "db+{}".format(self.SQLALCHEMY_DATABASE_URI)
            if self.CELERY_BACKEND == "database"
            else self.CELERY_BROKER_URL
        )

    @property
    def BROKER_USE_SSL(self) -> bool:
        return self.CELERY_BROKER_URL.startswith("rediss://") if self.CELERY_BROKER_URL else False


class MiddlewareConfig(
    CeleryConfig,
    DatabaseConfig,
    RedisConfig,
    MilvusConfig,
    ElasticsearchConfig
):
    pass
