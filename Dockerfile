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
RUN pip install --user --no-cache-dir -r requirements.txt
# 创建非 root 用户
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
# 切换到非 root 用户
USER appuser
# 数据库目录权限
RUN mkdir -p /app/data && chmod 755 /app/data
# 使用 Gunicorn 作为 WSGI 服务器
CMD ["gunicorn", "--bind", "0.0.0.0:10081", "--workers", "3", "ride_hailing_driver_examination.wsgi:application"]