# 这个文件用于定义 User 实体类，用于映射数据库中的 user 表

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    # 关于主键：虽然主键在数据库中不能为空，
    # 但由于 id 是数据库生成的，所以在 Python 中可以设置为 None
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    display_name: str | None
    hashed_password: str
    email: str | None
    disabled: bool | None
