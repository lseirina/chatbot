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
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal date', {'fields': ('email',)}),
        ('Permissions',
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )





if  admin.site.is_registered(User):
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)