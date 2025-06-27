#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: app_config
Time: 2025/6/27 17:06
"""

from pydantic_settings import SettingsConfigDict

from configs.deploy import DeploymentConfig
from configs.middleware import MiddlewareConfig
from configs.packaging import PackagingInfo


class AppConfig(
    PackagingInfo,
    DeploymentConfig,
    MiddlewareConfig
):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
