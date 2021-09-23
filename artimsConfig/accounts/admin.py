from django.contrib import admin 
from django.contrib.admin import ModelAdmin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from .models import *

# Register your models here.\
class customeUserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    
    list_display = ('name' ,'phone_number', 'is_active')
    list_filter = ('name', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('name', 'email')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions','role')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'email')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions','role')}),
    )
    search_fields = ('phone_number',)
    
    ordering = ('email',)
    filter_horizontal = ()

    


admin.site.register(customeUser, customeUserAdmin)


class roleAdmin(admin.ModelAdmin):
    fields = ('name',)

        
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        # Disable delete
        return False
    def has_add_permission(self, request ) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    
admin.site.register(role,roleAdmin) 


