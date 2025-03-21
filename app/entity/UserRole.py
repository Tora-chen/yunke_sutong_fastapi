# 这个文件定义了 UserRole 实体，用于存储每个用户的角色信息
# 由于一个用户可以有多个角色，一个角色也可以被多个用户拥有，所以这是一个多对多的关系
from sqlmodel import SQLModel, Field
class UserRole(SQLModel, table=True):
    __tablename__ = "user_role"
    id: int | None = Field(default=None, primary_key=True)
    role_id: str = Field(foreign_key="role.id")
    user_id: int = Field(foreign_key="user.id")