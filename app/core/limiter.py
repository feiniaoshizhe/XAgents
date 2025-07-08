#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module configures rate limiting using slowapi

Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: limiter
Time: 2025/7/7 13:05
"""

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])
