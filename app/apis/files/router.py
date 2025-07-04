#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: upload
Time: 2025/6/27 19:01
"""
from fastapi import APIRouter

from apis.files.schema import UploadFileDTO

router = APIRouter(prefix="/file")


@router.get("/upload", response_model=UploadFileDTO)
async def upload_files(

):
    pass
