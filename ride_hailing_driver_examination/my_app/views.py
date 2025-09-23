from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def login_view(request):
    if request.method == 'POST':
        id_card = request.POST['id_card']
        password = request.POST['password']
        # 验证身份证是否存在
        try:
            student = Student.objects.get(id_card=id_card)
        except Student.DoesNotExist:
            messages.error(request, '身份证号不存在')
            return render(request, 'login.html')
        # 验证密码
        if student.password == password:
            # 登录成功的逻辑, 使用 Django 的会话管理, 将学员ID存储在会话中
            request.session['student_id'] = student.id
            # 登录成功后重定向
            return redirect('home')
        messages.error(request, '密码错误')
    return render(request, 'login.html')
