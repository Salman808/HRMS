from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from payroll import views
from rest_framework.schemas import get_schema_view

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'designation', views.DesignationViewSet)
router.register(r'role-dept', views.DesigDeptViewSet)
router.register(r'company_policy', views.CompanyPolicyViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'leave', views.LeaveViewSet)
router.register(r'salary', views.SalaryViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'team-user', views.UserTeamViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'project-user', views.UserProjectViewSet)
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),

]
#
# department_list = DepartmentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# department_detail = DepartmentViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# role_list = RolesViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# role_detail = RolesViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# company_list = CompanyViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# company_detail = CompanyViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# salary = SalaryViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# salary_detail = SalaryViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# company_policy_list = CompanyPolicyViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# company_policy_detail = CompanyPolicyViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# attendance_list = AttendanceViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# attendance_detail = AttendanceViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# leave_list = LeaveViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# leave_detail = LeaveViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# role_dept_list = RoleDeptViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# role_dept_detail = RoleDeptViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })