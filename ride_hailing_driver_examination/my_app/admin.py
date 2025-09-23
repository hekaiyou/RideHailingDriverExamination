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

    def save_model(self, request, obj, form, change):
        # 通过 change 判断是否是新用户, 如果是新用户, 自动设置密码为身份证号后六位
        if not change and hasattr(obj, 'id_card'):
            # 获取身份证号后六位作为密码
            password = obj.id_card[-6:]
            # 使用 hash 处理密码
            obj.password = make_password(password)
        # 调用父类方法
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
