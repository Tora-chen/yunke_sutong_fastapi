# 这个文件用来存放Note相关的控制器

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlmodel import select

from app.entity import Note
from app.repository.database import SessionDep
from app.util.auth import has_role

router = APIRouter(
    prefix="/api/notes",
    tags=["notes"],  # API文档中的分类
    dependencies=[Depends(has_role("ROLE_STUDENT"))]
)

@router.get("/certainNote/{note_id}", deprecated=True) # 根据笔记ID查找笔记（弃用）
def find_certain_note(
    note_id: int,
    session: SessionDep,
    response: Response
) -> Note:
    # 由于不符合API命名规范，弃用该端点，使用 /api/notes/{note_id} 代替
    response.headers["X-API-Warning"] = "This endpoint is deprecated. Use /api/notes/{note_id} instead."
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/{note_id}") # 根据笔记ID查找笔记
def get_note(
    note_id: int,
    session: SessionDep,
) -> Note:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/videoNotes/{video_id}") # 根据视频ID查找该视频下的所有笔记
def find_video_notes(
    video_id: int,
    session: SessionDep,
) -> list[Note]:
    notes = session.exec(
        select(Note).where(Note.video_id == video_id)
    ).all()
    return notes

@router.post("/") # 创建一个新的笔记
def add_note(
    session: SessionDep,
    note: Note
) -> Note:
    session.add(note)
    session.commit()
    session.refresh(note)
    return note