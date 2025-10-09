## 开发流程

依赖安装:

```shell
% pip3 install Django
```

项目创建:

```shell
% django-admin startproject ride_hailing_driver_examination
% cd ride_hailing_driver_examination
% django-admin startapp my_app
```

数据库配置:

```shell
% cd ride_hailing_driver_examination
% python3 manage.py makemigrations
% python3 manage.py makemigrations my_app
% python3 manage.py migrate
```

管理员创建:

```shell
% cd ride_hailing_driver_examination
% python3 manage.py createsuperuser
% 用户名: admin
% 电子邮件地址: admin@example.com
% Password: **********
% Password (again): *********
```

启动服务:

```shell
% cd ride_hailing_driver_examination
# 使用默认IP和端口
% python3 manage.py runserver
# 使用自定义IP和端口
% python3 manage.py runserver 0.0.0.0:10081
```

## 安全设置

关闭调试模式运行:

ride_hailing_driver_examination\ride_hailing_driver_examination\settings.py
```python
DEBUG = False
```

指定可以访问应用程序的域名或 IP 地址:

ride_hailing_driver_examination\ride_hailing_driver_examination\settings.py
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'example.com', 'www.example.com']
```
