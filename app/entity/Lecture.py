# 这个文件用于定义 Lecture 实体类，用于映射数据库中的 lecture 表
# Lecture 是指一个课程，含有多个视频。

from sqlmodel import Field, SQLModel

class Lecture(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None
    uploader_id: int = Field(foreign_key="user.id")
    cover_path: str | None




