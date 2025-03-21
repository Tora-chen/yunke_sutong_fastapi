# 这个文件用于定义 Note 实体类，用于映射数据库中的 note 表。
# Note 是指视频下方的笔记栏，含有截图和截图的描述。

from sqlmodel import Field, SQLModel

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image_path: str | None
    description: str | None
    timestamp: str | None
    video_id: int