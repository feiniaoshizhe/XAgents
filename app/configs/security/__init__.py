#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: __init__.py
Time: 2025/7/7 9:15
"""
from pydantic import Field
from pydantic_settings import BaseSettings


class LangsmithConfig(BaseSettings):
    LANGSMITH_TRACING_V2: str = Field(default="true")

    LANGSMITH_API_KEY: str = Field()

    LANGSMITH_PROJECT: str = Field(default="xagent")


class LangfuseConfig(BaseSettings):
    LANGFUSE_PUBLIC_KEY: str = Field()

    LANGFUSE_SECRET_KEY: str = Field()

    LANGFUSE_HOST: str = Field(default="https://cloud.langfuse.com")


class SecurityConfig(
    LangfuseConfig,
    LangsmithConfig
):
    pass
