FROM python:3.10.12-slim as builder
# 设置工作目录
WORKDIR /app
# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gunicorn \
    && rm -rf /var/lib/apt/lists/*
# 复制项目文件
COPY . .
# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt
# 数据库目录权限
RUN mkdir -p /app/data && chmod 777 /app/data
# 进入项目目录
RUN cd ride_hailing_driver_examination
# 使用 Gunicorn 作为 WSGI 服务器
CMD ["gunicorn", "--bind", "0.0.0.0:10081", "--workers", "3", "ride_hailing_driver_examination.wsgi:application"]