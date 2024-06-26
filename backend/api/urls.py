from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, RoleHistoryViewSet, EmployeeSearchAPIView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

router2 = DefaultRouter()
router2.register(r'employees', EmployeeViewSet, basename='employee')

router3 = DefaultRouter()
router3.register(r'role-histories', RoleHistoryViewSet, basename='role-history')

urlpatterns = [
    path('employees/search/', EmployeeSearchAPIView.as_view(), name='employee-search'),
    # other URLs as needed
]

urlpatterns += router.urls + router2.urls + router3.urls
