import random
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.urls import reverse
from .models import Student, Course, Question, WrongAnswer
from .serializers import serialize_questions


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
    # 检查是否有提示信息
    show_message = request.GET.get('show_message', False)
    # 获取提示信息
    message = request.GET.get('message', None)
    context = {
        'course': course,
        'show_message': show_message,
        'message': message,
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
    # 使用序列化器将问题转换为 JSON 格式
    questions_json = serialize_questions(questions)
    context = {
        'course': course,
        'questions': questions_json,
    }
    return render(request, 'practice.html', context)


def exam_view(request, course_id):
    if 'student_id' not in request.session:
        return redirect('login')
    # 获取课程信息
    course = get_object_or_404(Course, id=course_id)
    # 获取课程下所有题目
    questions = list(course.questions.all())
    context = {
        'course': course,
        'questions': questions,
    }
    return render(request, 'exam.html', context)


def exam_rules_view(request, course_id):
    if 'student_id' not in request.session:
        return redirect('login')
    # 获取课程信息
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'exam_rules.html', context)


def wrong_questions_view(request, course_id):
    if 'student_id' not in request.session:
        return redirect('login')
    student = get_object_or_404(Student, id=request.session['student_id'])
    course = get_object_or_404(Course, id=course_id)
    # 获取当前用户在指定课程下的所有错题
    wrong_answers = student.wrong_answers.filter(course=course).select_related('question').all()
    # 如果没有错题, 重定向到学习页面并传递提示信息
    if not wrong_answers:
        # 设置提示信息
        message = "您没有错题, 继续加油!"
        return redirect(f"{reverse('study', args=[course.id])}?show_message=True&message={message}")
    # 获取全部错题对应的题目
    questions = [wrong_answer.question for wrong_answer in wrong_answers]
    # 随机化题目顺序
    random.shuffle(questions)
    # 使用序列化器将问题转换为 JSON 格式
    questions_json = serialize_questions(questions)
    context = {
        'course': course,
        'questions': questions_json,
    }
    return render(request, 'wrong_questions.html', context)


@csrf_protect
@require_POST
def add_wrong_question(request):
    data = json.loads(request.body)
    student_id = request.session.get('student_id')
    if not student_id:
        return JsonResponse({'error': '缺少学生ID'}, status=400)
    question_id = data.get('question_id')
    if not question_id:
        return JsonResponse({'error': '缺少题目ID'}, status=400)
    # 获取学生对象
    student = get_object_or_404(Student, id=student_id)
    # 获取题目对象
    question = get_object_or_404(Question, id=question_id)
    # 检查是否已经存在该错题记录
    existing_wrong_answer = WrongAnswer.objects.filter(student=student, question=question).first()
    if existing_wrong_answer:
        return JsonResponse({'message': '该错题已存在'}, status=200)
    # 如果不存在, 则创建新的错题记录
    try:
        WrongAnswer.objects.create(student=student, question=question, course=question.course)
        return JsonResponse({'message': '错题已添加'}, status=201)
    except Student.DoesNotExist:
        return JsonResponse({'error': '学员未登录'}, status=403)
    except Question.DoesNotExist:
        return JsonResponse({'error': '题目不存在'}, status=404)


@csrf_protect
@require_POST
def delete_wrong_question(request):
    data = json.loads(request.body)
    student_id = request.session.get('student_id')
    if not student_id:
        return JsonResponse({'error': '缺少学生ID'}, status=400)
    question_id = data.get('question_id')
    if not question_id:
        return JsonResponse({'error': '缺少题目ID'}, status=400)
    # 获取学生对象
    student = get_object_or_404(Student, id=student_id)
    # 获取错题记录
    try:
        wrong_answer = WrongAnswer.objects.get(student=student, question_id=question_id)
        wrong_answer.delete()
        return JsonResponse({'message': '错题已删除'}, status=200)
    except WrongAnswer.DoesNotExist:
        return JsonResponse({'error': '错题记录不存在'}, status=404)
