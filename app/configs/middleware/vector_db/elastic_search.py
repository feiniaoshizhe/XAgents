#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: elastic_search
Time: 2025/6/27 18:35
"""
from typing import Optional

from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings


class ElasticsearchConfig(BaseSettings):
    """
    Configuration settings for Elasticsearch
    """

    ELASTICSEARCH_HOST: Optional[str] = Field(default="127.0.0.1")

    ELASTICSEARCH_PORT: PositiveInt = Field(default=9200)

    ELASTICSEARCH_USERNAME: Optional[str] = Field(default="elastic")

    ELASTICSEARCH_PASSWORD: Optional[str] = Field(default="elastic")
