from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

'''Admin panel for USER'''
@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    ordering = ['id']
    list_display = [
        'id','email','first_name','last_name','is_staff','is_active',
    ]
    readonly_fields = ['id',]
    fieldsets = (
        (None,{
            'fields': ( 'id','email','first_name','last_name','is_staff','is_active'),
        }),
        
        
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name','password1', 'password2','is_staff',),
    }),
)