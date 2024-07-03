from django.contrib import admin
from .models import Company, Department, Employee, RoleHistory


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_date', 'registration_number', 'address', 'contact_person', 'phone', 'email')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id')


class RoleHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'company', 'department', 'role', 'date_started', 'date_left', 'duties')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RoleHistory, RoleHistoryAdmin)