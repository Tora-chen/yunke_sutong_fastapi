# 这个文件存放 Lecture 的控制器，用于处理和 Lecture 有关的请求

from typing import Annotated
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlmodel import select
from loguru import logger

from app.repository.database import SessionDep
from app.entity import Lecture, User
from app.util.auth import has_role


router = APIRouter(
    prefix="/api/lectures",
    tags=["lectures"],  # API文档中的分类
)


@router.post("/")  # 创建一个新的讲座
def create_lecture(
    session: SessionDep,  # 依赖注入，获取数据库会话

    current_user: Annotated[User, Depends(
        has_role("ROLE_STUDENT")
    )],  # 获取当前用户，要求用户角色为 ROLE_STUDENT

    title: Annotated[str, Body()],  # Body()表示从请求体中获取 title
    description: Annotated[str, Body()],
) -> Lecture:
    lecture = Lecture(
        title=title,
        description=description,
        uploader_id=current_user.id
    )
    session.add(lecture)
    session.commit()
    session.refresh(lecture)
    logger.info(f"{current_user.username} created a new lecture: {lecture}")
    return lecture


@router.delete("/{lecture_id}")  # 删除一个讲座
def delete_lecture(
    session: SessionDep,
    current_user: Annotated[User, Depends(has_role("ROLE_STUDENT"))],
    lecture_id: int
) -> dict[str, str]:
    lecture = session.get(Lecture, lecture_id)
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

    if lecture.uploader_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission denied")

    session.delete(lecture)
    session.commit()
    return {"message": "Lecture deleted successfully"}


@router.put("/{lecture_id}")  # 更新一个讲座
def update_lecture(
    session: SessionDep,
    current_user: Annotated[User, Depends(has_role("ROLE_STUDENT"))],
    lecture_id: int,  # 从路径参数中获取讲座 ID
    title: Annotated[str, Body()],
    description: Annotated[str, Body()]
) -> Lecture:
    lecture = session.get(Lecture, lecture_id)
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

    if lecture.uploader_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission denied")

    lecture.title = title
    lecture.description = description
    session.commit()
    session.refresh(lecture)
    return lecture


@router.get("/my")  # 获取当前用户上传的所有讲座
def get_my_lectures(
    session: SessionDep,
    current_user: Annotated[User, Depends(has_role("ROLE_STUDENT"))]
) -> list[Lecture]:
    lectures = session.exec(
        select(Lecture).where(Lecture.uploader_id == current_user.id)
    ).all()
    return lectures

# @router.get("/{lectureId}/videos") # 获取某个讲座的所有视频 TODO


@router.get("/recommendedLecture")  # 获取推荐的讲座
def get_recommended_lecture(
    session: SessionDep,
) -> list[Lecture]:
    # 从数据库中随机选取 count 个讲座
    count = 5
    lectures = session.exec(select(Lecture)).all()
    return lectures[:count]
