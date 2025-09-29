```shell
% pip3 install Django
```

```shell
% django-admin startproject ride_hailing_driver_examination
% cd ride_hailing_driver_examination
% django-admin startapp my_app
```

```shell
% cd ride_hailing_driver_examination
% python3 manage.py makemigrations
% python3 manage.py makemigrations my_app
% python3 manage.py migrate
```

```shell
% cd ride_hailing_driver_examination
% python3 manage.py createsuperuser
% 用户名: admin
% 电子邮件地址: admin@example.com
% Password: **********
% Password (again): *********
```

```shell
% cd ride_hailing_driver_examination
% python3 manage.py runserver
% python3 manage.py runserver 0.0.0.0:10081
```
