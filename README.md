# FastAPI 微服务演示项目 / FastAPI Microservices Demo Project

## 项目简介 / Project Overview

这是一个基于 FastAPI 的微服务架构演示项目，展示了如何使用 Docker Compose 构建和部署现代化的 Web 应用程序。项目采用了反向代理、数据库集成、CI/CD 自动化部署等最佳实践。

This is a FastAPI-based microservices architecture demo project that demonstrates how to build and deploy modern web applications using Docker Compose. The project incorporates best practices including reverse proxy, database integration, and CI/CD automated deployment.

## 技术栈 / Tech Stack

- **后端框架 / Backend Framework**: FastAPI
- **数据库 / Database**: PostgreSQL
- **ORM**: SQLModel
- **反向代理 / Reverse Proxy**: Nginx
- **容器化 / Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Python 版本 / Python Version**: 3.13.2

## 项目架构 / Project Architecture

```
fastapi_test/
├── backend_services/           # 后端服务目录 / Backend services directory
│   ├── diary_service/         # 日记服务 / Diary service
│   ├── agent_service/         # 代理服务 / Agent service (预留)
│   ├── media_service/         # 媒体服务 / Media service (预留)
│   └── todo_service/          # 待办事项服务 / Todo service (预留)
├── reverse_proxy/             # Nginx 反向代理配置 / Nginx reverse proxy config
├── .github/workflows/         # CI/CD 工作流 / CI/CD workflows
└── compose files              # Docker Compose 配置文件 / Docker Compose configs
```

## 核心功能 / Core Features

### 日记服务 / Diary Service

日记服务提供了完整的 CRUD API，用于管理事件记录：

The diary service provides a complete CRUD API for managing event records:

- **GET** `/api/events/` - 获取所有事件列表 / Get all events list
- **POST** `/api/events/` - 创建新事件 / Create new event
- **GET** `/api/events/{event_id}` - 获取特定事件 / Get specific event
- **PUT** `/api/events/{event_id}` - 更新事件 / Update event
- **DELETE** `/api/events/{event_id}` - 删除事件 / Delete event

### 数据模型 / Data Model

```python
class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""
```

## 快速开始 / Quick Start

### 前置要求 / Prerequisites

- Docker
- Docker Compose
- Git

### 安装和运行 / Installation and Running

1. **克隆项目 / Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi_test
   ```

2. **创建环境变量文件 / Create environment file**
   ```bash
   cp .env.compose.example .env.compose
   ```
   
   编辑 `.env.compose` 文件，配置必要的环境变量。
   
   Edit the `.env.compose` file to configure necessary environment variables.

3. **启动服务 / Start services**
   
   **开发环境 / Development environment:**
   ```bash
   docker-compose -f compose.dev.yml up --build
   ```
   
   **生产环境 / Production environment:**
   ```bash
   docker-compose -f compose.prod.yaml up --build
   ```

4. **访问应用 / Access the application**
   
   应用将在 `http://localhost:8080` 启动
   
   The application will be available at `http://localhost:8080`

### API 文档 / API Documentation

启动服务后，可以通过以下地址访问 API 文档：

After starting the services, you can access the API documentation at:

- Swagger UI: `http://localhost:8080/api/v1/diary/docs`
- ReDoc: `http://localhost:8080/api/v1/diary/redoc`

## 服务配置 / Service Configuration

### 数据库配置 / Database Configuration

- **用户名 / Username**: `user_test`
- **密码 / Password**: `pw_test`
- **数据库名 / Database**: `MyPostgresql`
- **端口 / Port**: `5432` (内部网络)

### 健康检查 / Health Check

项目包含健康检查端点：

The project includes health check endpoints:

- 应用健康检查 / Application health: `GET /healthz`
- 数据库健康检查 / Database health: 自动配置 / Automatically configured

## 开发指南 / Development Guide

### 添加新服务 / Adding New Services

1. 在 `backend_services/` 目录下创建新的服务目录
2. 添加 Dockerfile 和 requirements.txt
3. 在 `compose.yaml` 中配置新服务
4. 更新 Nginx 配置以添加路由规则

1. Create a new service directory under `backend_services/`
2. Add Dockerfile and requirements.txt
3. Configure the new service in `compose.yaml`
4. Update Nginx configuration to add routing rules

### 本地开发 / Local Development

```bash
# 进入服务目录 / Enter service directory
cd backend_services/diary_service

# 安装依赖 / Install dependencies
pip install -r requirements.txt

# 启动开发服务器 / Start development server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8002
```

## CI/CD 部署 / CI/CD Deployment

项目配置了 GitHub Actions 自动化部署流程：

The project is configured with GitHub Actions automated deployment workflow:

- **触发条件 / Trigger**: 推送到 main 分支 / Push to main branch
- **构建 / Build**: 自动构建 Docker 镜像 / Automatically build Docker images
- **部署 / Deploy**: 推送到容器注册表 / Push to container registry

### 配置 Secrets / Configure Secrets

在 GitHub 仓库设置中添加以下 secrets：

Add the following secrets in your GitHub repository settings:

- `DOCKER_REGISTRY`: Docker 注册表地址 / Docker registry URL
- `DOCKER_USERNAME`: Docker 用户名 / Docker username
- `GITHUB_TOKEN`: 自动生成 / Auto-generated

## 许可证 / License

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 贡献 / Contributing

欢迎提交 Pull Request 和 Issue！

Pull requests and issues are welcome!

## 联系方式 / Contact

如有问题或建议，请通过 GitHub Issues 联系。

For questions or suggestions, please contact via GitHub Issues.

        