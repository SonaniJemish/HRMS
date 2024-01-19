from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Designation


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields =('username', 'pk')
    filter_horizontal =()
    fieldsets = ()
    list_per_page = 20

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Designation)
admin.site.register(Department)
