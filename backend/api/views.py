from rest_framework import viewsets
from .models import Company, Employee, RoleHistory
from .serializers import CompanySerializer, EmployeeSerializer, RoleHistorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RoleHistoryViewSet(viewsets.ModelViewSet):
    queryset = RoleHistory.objects.all()
    serializer_class = RoleHistorySerializer


