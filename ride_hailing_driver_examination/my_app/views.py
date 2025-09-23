from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        id_card = request.POST['id_card']
        password = request.POST['password']
        # 判断用户名和密码
        user = authenticate(request, username=id_card, password=password)
        if user is not None:
            login(request, user)
            # 登录成功后重定向至主页
            return redirect('home')
        else:
            messages.error(request, '身份证号或密码错误')
    # 渲染登录页面
    return render(request, 'login.html')
