from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DepartmentViewSet, EmployeeViewSet, RoleHistoryViewSet, EmployeeSearchAPIView

router1 = DefaultRouter()
router1.register(r'companies', CompanyViewSet, basename='company')

router2 = DefaultRouter()
router2.register(r'departments', DepartmentViewSet, basename='department')

router3 = DefaultRouter()
router3.register(r'employees', EmployeeViewSet, basename='employee')

router4 = DefaultRouter()
router4.register(r'role-histories', RoleHistoryViewSet, basename='role-history')

urlpatterns = [
    path('employees/search/', EmployeeSearchAPIView.as_view(), name='employee-search'),
    # other URLs as needed
]

urlpatterns += router1.urls + router2.urls + router3.urls + router4.urls
