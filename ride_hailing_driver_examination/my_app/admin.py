from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        ('学员信息', {'fields': ('id_card', 'occupation_type',)}),
    ) + UserAdmin.fieldsets
    add_fieldsets = (
        ('学员信息', {'fields': ('id_card', 'occupation_type',)}),
    ) + UserAdmin.add_fieldsets
    # 这里添加显示列表属性
    list_display = ('username', 'id_card', 'occupation_type')
    # 允许根据用户名和身份证号搜索
    search_fields = ('username', 'id_card')

admin.site.register(CustomUser, CustomUserAdmin)
