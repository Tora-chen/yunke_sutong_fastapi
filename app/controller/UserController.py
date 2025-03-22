# 这个文件存放用户身份认证相关的控制器

from datetime import timedelta

from fastapi import APIRouter, HTTPException, status, Form
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlmodel import select

from app.util.auth import Token, authenticate_user, create_access_token
from app.repository.database import Session, get_session, SessionDep
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.entity import User
from app.util.auth import get_password_hash


router = APIRouter(
    tags=["users"] # API文档中的分类
)

@router.post("/api/login") # 登录
async def login(
    session: Annotated[Session, Depends(get_session)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 签发 JWT 令牌
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.post("/api/register") # 注册
async def register(
    session: SessionDep,
    username: str = Form(),
    display_name: str = Form(),
    password: str = Form(),
    email: str = Form()
) -> User:
    # 检查用户名是否已存在
    user = session.exec(
        select(User).where(User.username == username)
    ).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    # 创建新用户
    hashed_password = get_password_hash(password)
    user = User(
        username = username, 
        hashed_password = hashed_password, 
        email = email,
        display_name = display_name
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

    