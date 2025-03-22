from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import select

from app.entity import Caption, User, Video
from app.repository.database import SessionDep
from app.util.auth import has_role

router_student = APIRouter(
    prefix="/api/captions",
    tags=["captions"],
    dependencies=[Depends(has_role("ROLE_STUDENT"))]
)

router_video_processor = APIRouter(
    prefix="/api/captions",
    tags=["captions_video_processor"],
    dependencies=[Depends(has_role("ROLE_VIDEO_PROCESSOR"))]
)


@router_student.get("/")
def get_caption(
    session: SessionDep,
    video_id: int,
    lang: str = 'default'
) -> Caption:
    caption: Caption = session.exec(
        select(Caption).where(Caption.video_id == video_id, Caption.lang == lang)
    ).first()
    return caption

@router_video_processor.post("/")  # 创建一个新的字幕
def add_caption(
        session: SessionDep,
        caption_path: Annotated[str, Body()],
        video_path: Annotated[str, Body()],
        caption_lang: Annotated[str, Body()] = 'default',
) -> Caption:
    video = session.exec(
        select(Video).where(Video.path == video_path)
    ).first()

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    caption = Caption(
        path=caption_path,
        language=caption_lang,
        video_id=video.id
    )

    session.add(caption)
    session.commit()
    session.refresh(caption)
    return caption
