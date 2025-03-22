# 这个文件定义了一个 Caption 类，用于存储字幕的描述信息

from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint
class Caption(SQLModel, table=True):
    __table_args__ = (
        # 联合唯一约束，保证同一视频的同一语言字幕只有一份
        UniqueConstraint("language", "video_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    path: str
    language: str = Field(default="default")
    video_id: int = Field(foreign_key="video.id")