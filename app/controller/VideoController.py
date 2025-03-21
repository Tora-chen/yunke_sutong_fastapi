from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/api/videos",
    tags=["videos"],  # API文档中的分类
)
