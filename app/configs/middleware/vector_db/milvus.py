#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: milvus
Time: 2025/6/27 18:35
"""
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class MilvusConfig(BaseSettings):
    """
     Configuration settings for Milvus
    """
    MILVUS_URI: Optional[str] = Field(default="http://milvus-master:19530")

    MILVUS_TOKEN: Optional[str] = Field(default=None)

    MILVUS_USER: Optional[str] = Field(default=None)

    MILVUS_PASSWORD: Optional[str] = Field(default=None)

    MILVUS_DATABASE: str = Field(default="default")

    MILVUS_ENABLE_HYBRID_SEARCH: bool = Field(default=True)

    MILVUS_ANALYZER_PARAMS: Optional[str] = Field(default="chinese")
