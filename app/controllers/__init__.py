#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: __init__.py
Time: 2025/6/27 13:58
"""
from fastapi import APIRouter

app_router = APIRouter(prefix="/api")
mcp_router = APIRouter(prefix="/mcp")
