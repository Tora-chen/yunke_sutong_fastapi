from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from loguru import logger

from app.repository.database import engine, create_db_and_tables, execute_sql_file
from app.controller import LectureController, UserController
from app.entity import *


@asynccontextmanager  # 生命周期管理，指定在应用启动和关闭时执行的操作
async def lifespan(app: FastAPI):
    logger.info("Creating database and tables...")

    SQLModel.metadata.drop_all(engine)  # 删除所有表
    create_db_and_tables()  # 创建数据库和表
    execute_sql_file("data.sql")  # 执行 data.sql 文件

    logger.info("Database and tables created")
    yield

app = FastAPI(lifespan=lifespan)

# 注册路由
app.include_router(LectureController.router)
app.include_router(UserController.router)


@app.get("/")
async def root():
    return {"message": "Hello! I am the API server of Yunke_Sutong."}
