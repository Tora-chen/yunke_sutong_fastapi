# 这个文件负责数据库连接与初始化，使用了 sqlmodel 库。
# 关于 sqlmodel 库的使用，可以参考官方文档：https://sqlmodel.fastapi.org.cn/

from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from app.config import SQLITE_URL, ECHO_SQL

connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, echo=ECHO_SQL, connect_args=connect_args)

def execute_sql_file(sql_file: str):
    conn = engine.raw_connection()  # 获取底层数据库连接
    try:
        cursor = conn.cursor()
        with open(sql_file, "r", encoding="utf-8") as f:
            sql_script = f.read()
        cursor.executescript(sql_script)  # 执行整个 SQL 脚本
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
