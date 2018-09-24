from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(id=self.request.user.id)
        else:
            return self.queryset

    def perform_update(self, serializer):
        serializer.save()
        print(type(User))
        usr = User.objects.get(id=serializer.data['id']).set_password(raw_password=
                                                                serializer.data['password'])

    def perform_create(self, serializer):
        usr = User.objects.create_user(username=serializer.validated_data['username'],
                                  email=serializer.validated_data['email'],
                                  password=serializer.validated_data['password'],
                                  first_name=serializer.validated_data['first_name'],
                                  last_name=serializer.data['last_name'],
                                  dob=serializer.data['dob'],
                                  dept_id=serializer.data['dept_id'],
                                  role_id=serializer.data['role_id'],
                                  mobileno=serializer.data['mobileno'],
                                  fathername=serializer.data['fathername'],
                                  manager_id=serializer.data['manager_id'],
                                  gender=serializer.data['gender']
                                  )
        usr.groups.set(serializer.data['groups'])


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        if self.request.user.is_anonymous:
            return []
        if self.request.user.dept_id:
            id = self.request.user.dept_id
            dept = Departments.objects.all().filter(id=id)
            cid = dept.companyid
        else:
            cid = 0
        return self.queryset.filter(companyid=cid)


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer


class UserProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        if 'name' in kwargs:
           self.queryset = Attendance.objects.all().filter(emp_id__first_name__contains=kwargs['name'])
        if 'dept_id' in kwargs:
            self.queryset = Attendance.objects.all().filter(emp_id__department=kwargs['dept_id'])
        if 'project_id' in kwargs and 'team_id' in kwargs:
            self.queryset = Attendance.objects.all().filter(team_id=kwargs['team_id'])
        else:
            if 'team_id' in kwargs:
                self.queryset = Attendance.objects.all().filter(team_id=kwargs['team_id'])
            if 'project_id' in kwargs:
                self.queryset = Attendance.objects.all().filter(project_id=kwargs['project_id'])
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leaves.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class CompanyPolicyViewSet(viewsets.ModelViewSet):
    queryset = CompanyPolicy.objects.all()
    serializer_class = CompanyPolicySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class DesigDeptViewSet(viewsets.ModelViewSet):
    queryset = DesigDept.objects.all()
    serializer_class = DesigDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)



