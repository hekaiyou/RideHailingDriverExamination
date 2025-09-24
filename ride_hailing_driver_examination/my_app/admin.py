from django.contrib import admin
from .models import Student, Course, Question, WrongAnswer


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_card', 'profession_type',)
    search_fields = ('name', 'id_card',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_type',)
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('题目详情', {'fields': ('course', 'text', 'question_type',)}),
        ('判断题', {'fields': ('is_correct',)}),
        ('选择题', {'fields': ('option_a', 'a_correct','option_b', 'b_correct', 'option_c', 'c_correct', 'option_d', 'd_correct', 'option_e', 'e_correct', 'option_f', 'f_correct')}),
    )
    add_fieldsets = (
        ('题目详情', {'fields': ('course', 'text', 'question_type',)}),
        ('判断题', {'fields': ('is_correct',)}),
        ('选择题', {'fields': ('option_a', 'a_correct','option_b', 'b_correct', 'option_c', 'c_correct', 'option_d', 'd_correct', 'option_e', 'e_correct', 'option_f', 'f_correct')}),
    )
    list_display = ('text', 'question_type',)
    search_fields = ('text',)
    list_filter = ('question_type', 'course')


@admin.register(WrongAnswer)
class WrongAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'answered_at',)
    search_fields = ('student__name', 'question__text',)
    list_filter = ('answered_at',)
