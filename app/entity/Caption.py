# 这个文件定义了一个 Caption 类，用于存储字幕的描述信息

from sqlmodel import SQLModel, Field
class Caption(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    path: str
    language: str = Field(default="default")
    video_id: int = Field(foreign_key="video.id")