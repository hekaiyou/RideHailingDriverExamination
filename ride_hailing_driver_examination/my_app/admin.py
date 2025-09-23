from django.contrib import admin
from .models import Student, Course, Question


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'profession_type',)
    search_fields = ('id_card',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_type',)
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type',)
    search_fields = ('text',)
    list_filter = ('question_type', 'course')
