from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'profession_type', 'password',)
    search_fields = ('id_card',)
