from django.contrib import admin
from database import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

'''Admin panel for USER'''


@admin.register(models.User)
class UserAdmin(UserAdmin):
    ordering = ['id']
    list_display = [
        'id', 'email', 'first_name', 'last_name', 'contact_no', 'is_staff', 'is_active', 'created_at', 'updated_at', 'user_profile',
    ]
    readonly_fields = ['id',]
    fieldsets = (
        (None, {
            'fields': ('id', 'email', 'first_name', 'last_name', 'contact_no', 'is_staff', 'is_active', 'user_profile'),
        }),


    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'contact_no', 'user_profile', 'password1', 'password2', 'is_staff',),
        }),
    )
