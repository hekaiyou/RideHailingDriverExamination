"""
URL configuration for ride_hailing_driver_examination project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录视图
    path('login/', views.login_view, name='login'),
    # 首页视图
    path('home/', views.home_view, name='home'),
    # 个人视图
    path('profile/', views.profile_view, name='profile'),
    # 退出登录视图
    path('logout/', views.logout_view, name='logout'),
    # 学习视图
    path('study/<int:course_id>/', views.study_view, name='study'),
    # 顺序练习视图
    path('practice/<int:course_id>/', views.practice_view, name='practice'),
    # 模拟考试视图
    path('exam/<int:course_id>/', views.exam_view, name='exam'),
    # 模拟考试规则视图
    path('exam-rules/<int:course_id>/', views.exam_rules_view, name='exam_rules'),
]
