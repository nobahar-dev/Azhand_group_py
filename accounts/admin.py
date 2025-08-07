from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .admin_forms import *
from .models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = EditUserForm
    add_form = CreateUserForm
    
    list_display = ('username', 'email', 'work_position', 'personnel_code')
    list_filter = ('work_position', )
    
    fieldsets = (
        ('Accounts Info', {'fields': ('username', 'email', 'password')}),
        ('Personal Information', {'fields': ('profile_image', 'first_name', 'last_name', 'work_position', 'personnel_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')})
    )
    
    add_fieldsets = (
        ('Add User', {'fields': ('username', 'email', 'password1', 'password2')}),
    )
    
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions')