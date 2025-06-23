#!/bin/bash

# 激活之前创建的 Python 虚拟环境
# 确保我们使用的是 /opt/venv 中的 Python 解释器和库
source /opt/venv/bin/activate

# 切换到应用程序代码目录
# 虽然 Dockerfile 中已经设置了 WORKDIR，但在这里再次确认可以使脚本更健壮
cd /code

# 设置运行端口。如果环境变量 "PORT" 存在，则使用其值；否则，默认使用 8000
RUN_PORT=${PORT:-8000}

# 设置运行主机。如果环境变量 "HOST" 存在，则使用其值；否则，默认使用 0.0.0.0
# 0.0.0.0 是一个特殊的地址，它告诉服务器监听所有可用的网络接口，这在容器环境中是必需的。
RUN_HOST=${HOST:-0.0.0.0}

# 使用 Gunicorn 启动应用
# Gunicorn 是一个生产级的 WSGI HTTP 服务器。
# -k uvicorn.workers.UvicornWorker: 指定使用 Uvicorn 作为工作进程。Uvicorn 是一个 ASGI 服务器，
#   用于运行像 FastAPI 这样的异步 Python Web 框架。Gunicorn 负责管理这些 Uvicorn 进程。
# -b $RUN_HOST:$RUN_PORT: 将服务器绑定到指定的主机和端口。
# main:app: 告诉 Gunicorn 在 main.py 文件中寻找一个名为 app 的应用实例来运行。
gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app
