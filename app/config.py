# 这个文件用于从toml配置文件中读取配置信息

import tomllib
from pathlib import Path
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent  # 项目根目录
CONFIG_PATH = BASE_DIR / "config.toml"

try:
    with open(CONFIG_PATH, 'rb') as f:
        config = tomllib.load(f)
except Exception as e:
    logger.error(f"Failed to load config file: {e}")
    raise e

    

# 安全配置
SECRET_KEY = config["security"]["secret_key"]
ALGORITHM = config["security"]["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = config["security"]["access_token_expire_minutes"]

# 数据库配置
SQLITE_URL = config["database"]["sqlite_url"]
ECHO_SQL = config["database"]["echo_sql"]