#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: router
Time: 2025/7/4 13:45
"""
import logging

from fastapi import APIRouter, Request

from apis.agents.schema import ChatRequest, ChatResponse

router = APIRouter(prefix="/agent")

logger = logging.getLogger("agent router")


@router.post("/chat", response_model=ChatResponse)
async def chat(
        request: Request,
        chat_request: ChatRequest,
        # session: Session = Depends(get_current_session),
):
    pass
