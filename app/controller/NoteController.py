# 这个文件用来存放Note相关的控制器

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from app.entity import Note
from app.repository.database import SessionDep
from app.util.auth import has_role

router = APIRouter(
    prefix="/api/notes",
    tags=["notes"],  # API文档中的分类
    dependencies=[Depends(has_role("ROLE_STUDENT"))]
)

@router.get("/certainNote/{note_id}")
def find_certain_note(
    note_id: int,
    session: SessionDep,
) -> Note:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/videoNotes/{video_id}")
def find_video_notes(
    video_id: int,
    session: SessionDep,
) -> list[Note]:
    notes = session.exec(
        select(Note).where(Note.video_id == video_id)
    ).all()
    return notes
