#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: __init__.py
Time: 2025/7/7 9:48
"""

from langchain_core.tools.base import BaseTool

from core.langgraph.tools.duckduckgo_search import duckduckgo_search_tool

tools: list[BaseTool] = [duckduckgo_search_tool]
