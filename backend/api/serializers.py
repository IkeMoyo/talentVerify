from rest_framework import serializers
from .models import Company, Department, Employee, RoleHistory


class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        return RoleHistory.objects.filter(company=obj, date_left__isnull=True).count()


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RoleHistorySerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = RoleHistory
        fields = '__all__'

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data.get('date_left') and data['date_left'] < data['date_started']:
            raise serializers.ValidationError("Date left cannot be before date started.")
        return data
