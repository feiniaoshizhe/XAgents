#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: base
Time: 2025/7/4 14:30
"""
from sqlalchemy import MetaData, Column, TIMESTAMP, String
from sqlalchemy.orm import declarative_base

# PostgreSQL索引命名约定
POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",  # 索引命名格式：列名_idx
    "uq": "%(table_name)s_%(column_0_name)s_key",  # 唯一约束命名格式：表名_列名_key
    "ck": "%(table_name)s_%(constraint_name)s_check",  # 检查约束命名格式：表名_约束名_check
    "fk": "%(table_name)s_%(column_0_name)s_fkey",  # 外键命名格式：表名_列名_fkey
    "pk": "%(table_name)s_pkey",  # 主键命名格式：表名_pkey
}

# 创建带有自定义命名约定的元数据对象
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

DeclarativeBase = declarative_base()


class BaseModel(DeclarativeBase):
    metadata = metadata

    create_time = Column(TIMESTAMP(timezone=False), server_default=func.now(), doc="Creation time")
    update_time = Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), doc="Update time")
    created_by = Column(String(100))
    updated_by = Column(String(100))
    is_deleted = Column()
