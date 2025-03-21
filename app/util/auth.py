# 这个文件定义了用于用户认证的工具函数，包括密码验证、JWT 令牌生成、用户认证等功能

from typing import Annotated, Callable, Sequence
from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlmodel import select
from pydantic import BaseModel

from app.entity import *
from app.repository.database import SessionDep, get_session
from app.config import SECRET_KEY, ALGORITHM


# OAuth2PasswordBearer用于从请求中提取令牌，tokenUrl指定登录路径
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

# 将加密算法指定为 bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    # 将传入的密码与数据库中的密码进行比较
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    # 获取密码哈希值
    return pwd_context.hash(password)


def authenticate_user(session: SessionDep, username: str, password: str):
    # 通过用户名获取用户信息
    user = session.exec(
        select(User).where(User.username == username)
    ).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # 生成 JWT 令牌
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


class Token(BaseModel):
    # 定义 Token 模型
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # 定义 TokenData 模型
    username: str | None = None


async def get_current_user(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    # 从请求中提取令牌，并从中解析出用户信息
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = session.exec(
        select(User).where(User.username == token_data.username)
    ).first()

    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def has_role(
    role_name: str,
) -> Callable:
    # 定义一个角色检查依赖
    # 由于Depends装饰器无法传递参数，因此需要定义一个函数，返回一个带参数的函数
    # 该函数接受一个角色名作为参数，返回一个带有session和current_user参数的函数
    # session和current_user参数是FastAPI框架自动传入的
    async def has_role_role_name(
            session: SessionDep,
            current_user: User = Depends(get_current_user)
    ) -> User:
        roles: Sequence[Role] | None = session.exec(
            select(Role)
            .join(UserRole, Role.id == UserRole.role_id)
            .where(UserRole.user_id == current_user.id)
        ).all()
        if not roles or role_name not in [r.name for r in roles]:
            raise HTTPException(status_code=403, detail="Permission denied")
        return current_user
    return has_role_role_name
