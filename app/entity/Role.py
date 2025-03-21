# 这个文件定义了一个 Role 类。
# Role 表示用户的身份，比如管理员、普通用户，用于权限控制。

from sqlmodel import SQLModel, Field
class Role(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str