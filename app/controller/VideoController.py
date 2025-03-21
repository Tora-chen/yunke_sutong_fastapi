from fastapi import APIRouter

router = APIRouter(
    prefix="/api/videos",
    tags=["videos"],  # API文档中的分类
)
