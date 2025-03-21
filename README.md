## 云课速通-FastAPI

> 一个使用 **FastAPI** 开发的课程平台后端服务，支持 JWT 认证、数据库操作、API 文档等功能。


---

## 🚀 技术栈

- **后端框架**：[FastAPI](https://fastapi.org.cn/)  
- **数据库**：SQLite3
- **ORM**：[SQLModel](https://sqlmodel.cn/)
- **身份认证**：JWT（使用 PyJWT）  
- **日志管理**：[loguru](https://loguru.readthedocs.io/)
- **配置管理**：[TOML](https://toml.io/cn/)   

---

## 📂 目录结构

```bash
📦 项目根目录
├── 📁 .vscode          # vscode运行配置
├── 📁 app              # 主要应用代码
│   ├── 📁 controller   # API 相关路由
│   ├── 📁 entity       # 实体模型
│   ├── 📁 repository   # 数据库操作
│   ├── 📁 util         # 工具函数
│   ├── config.py       # 加载配置文件
│   └── main.py         # 入口文件
├── .gitignore          # Git 忽略文件
├── data.sql            # 数据库初始化脚本
├── example.config.toml # 配置文件示例
├── requirements.txt    # Python 依赖包
└── README.md           # 项目文档
```

---

## 🔧 环境配置

### 1️⃣ **克隆项目**
```sh
git clone https://github.com/Tora-chen/yunke_sutong_fastapi
cd yunke_sutong_fastapi
```

### 2️⃣ **创建虚拟环境**
Linux:
```sh
python -m venv .venv
source .venv/bin/activate
```
Windows:
```sh
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ **安装依赖**
```sh
pip install -r requirements.txt
```

### 4️⃣ **修改配置文件**
在根目录创建 `config.toml` 文件，将 `example.config.toml` 中的内容复制到 `config.toml` 中，并修改其中的配置。

---

## 🚀 运行项目

### **开发模式**
如果你使用`VSCode`，项目中写有运行配置，可以直接使用`F5`运行项目。

或者在终端中输入命令：
```sh
uvicorn app.main:app --reload
```

---

## 🔍 查看 API 文档

项目启动后，可以在浏览器中访问交互式 API 文档：

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

