#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: packaging
Time: 2025/6/27 17:09
"""
from pydantic import Field
from pydantic_settings import BaseSettings


class PackagingInfo(BaseSettings):
    CURRENT_VERSION: str = Field(
        description="fast rag version",
        default="1.0.0"
    )
