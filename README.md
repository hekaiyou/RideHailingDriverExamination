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
% python3 manage.py runserver
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

## 快速部署

创建名为 `rhde` 的 **Linux screen** 视窗:

```shell
% screen -S rhde
```

在 **Linux screen** 视窗中启动服务:

```shell
% cd ride_hailing_driver_examination
% python3 manage.py runserver 0.0.0.0:10081
```

或者可以通过 **Gunicorn** 启动服务, 以获得更好的性能:

```shell
% cd ride_hailing_driver_examination
% gunicorn --bind 0.0.0.0:10081 --workers 3 ride_hailing_driver_examination.wsgi:application
```

通过 *Ctrl+A -> Ctrl+D* 退出当前视窗, 下次可以通过命令回到名为 rhde 的视窗:

```shell
% screen -r rhde
```

取消部署时, 先进入视窗再通过 *Ctrl+D* 删除当前视窗。
