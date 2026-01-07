from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from app.models import *

@admin.register(Usercustome)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('phone_number', 'role')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('phone_number', 'role')}),
    )

    list_display = ('username', 'email', 'phone_number', 'role')
    

admin.site.register(UserProfile)    
    
# class CustomUserAdmin(UserAdmin):
#     model = Usercustome
#     list_display = ('id','username', 'email', 'phone_number','role')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number', 'role')}),
#     )
    
# admin.site.register(Usercustome, CustomUserAdmin)
    
    
    