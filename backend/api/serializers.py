from rest_framework import serializers
from .models import Company, Department, Employee, RoleHistory


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RoleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleHistory
        fields = '__all__'

