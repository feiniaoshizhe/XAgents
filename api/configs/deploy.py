#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: deploy
Time: 2025/6/27 17:12
"""
import logging

from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings


class DeploymentConfig(BaseSettings):
    DEBUG: bool = Field(default=False)
    ENV: str = Field(default="production")
    SERVER_HOST: str = Field(default="127.0.0.1")
    SERVER_PORT: PositiveInt = Field(default=10001)
    SERVER_WORKERS: int = Field(default=1)
    LOGGING_LEVEL: int = logging.INFO
