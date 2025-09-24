import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Course


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


def home_view(request):
    if 'student_id' not in request.session:
        # 如果用户未登录, 则重定向到登录页面
        return redirect('login')
    # 获取所有课程
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'home.html', context)


def profile_view(request):
    if 'student_id' not in request.session:
        # 如果用户未登录, 则重定向到登录页面
        return redirect('login')
    student = Student.objects.get(id=request.session['student_id'])
    context = {
        'student': student,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    try:
        del request.session['student_id']
    except KeyError:
        pass
    return redirect('login')


def study_view(request, course_id):
    if 'student_id' not in request.session:
        # 未登录用户重定向到登录
        return redirect('login')
    # 获取课程对象
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'study.html', context)


def practice_view(request, course_id):
    if 'student_id' not in request.session:
        return redirect('login')
    # 获取课程和相关问题
    course = get_object_or_404(Course, id=course_id)
    # 获取课程下所有题目
    questions = list(course.questions.all())
    # 随机化题目顺序
    random.shuffle(questions)
    context = {
        'course': course,
        'questions': questions,
    }
    print(context)
    return render(request, 'practice.html', context)
