# 这个文件定义了 Video 实体类，用于映射数据库中的 video 表
# Video 属于 Lecture，每个 Lecture 内有若干 Video。

from sqlmodel import SQLModel, Field

class Video(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    transcript: str
    path: str
    lecture_id: int = Field(foreign_key="lecture.id")
