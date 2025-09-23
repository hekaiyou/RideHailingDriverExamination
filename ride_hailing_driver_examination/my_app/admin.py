from django.contrib import admin
from .models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'profession_type',)
    search_fields = ('id_card',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_subject', 'question_count',)
    search_fields = ('name', 'exam_subject',)
