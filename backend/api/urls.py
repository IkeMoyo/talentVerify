from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, RoleHistoryViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

router2 = DefaultRouter()
router2.register(r'employees', EmployeeViewSet, basename='employee')

router3 = DefaultRouter()
router3.register(r'role-histories', RoleHistoryViewSet, basename='role-history')

urlpatterns = router.urls + router2.urls + router3.urls
