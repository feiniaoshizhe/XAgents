#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: router
Time: 2025/7/4 13:45
"""
import logging

from fastapi import APIRouter

router = APIRouter(prefix="/agent")

logger = logging.getLogger("agent router")
