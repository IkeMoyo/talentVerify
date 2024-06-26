from django.contrib import admin
from .models import Company, Employee, RoleHistory


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_registration', 'registration_number', 'address', 'contact_person', 'phone', 'email')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'company', 'department')


class RoleHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'role', 'date_started', 'date_left', 'duties')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RoleHistory, RoleHistoryAdmin)