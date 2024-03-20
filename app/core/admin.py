"""
Django admin customazation
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UserAdmin(BaseUserAdmin):
    """Define admin pages for user."""
    ordering = ['id']
    list_display = ['username']

if  admin.site.is_registered(User):
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)