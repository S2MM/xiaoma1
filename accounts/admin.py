from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = [
        (None, {'fields': ('email', 'username', 'password')}),
        ('个人信息', {'fields': ('first_name', 'last_name')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要数据', {'fields': ('last_login', 'date_joined')}),
    ]

    list_display = ('id', 'email', 'username', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('id',)