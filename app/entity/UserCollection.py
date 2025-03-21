# 这个文件定义了 UserCollection 实体类，用于映射数据库中的 user_collection 表
# 由于一个用户可以收藏多个讲座，一个讲座也可以被多个用户收藏，所以这是一个多对多的关系

from sqlmodel import SQLModel, Field
class UserCollection(SQLModel, table=True):
    __tablename__ = "user_collection" # 指定表名，否则默认为 usercollection
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    lecture_id: int = Field(foreign_key="lecture.id")