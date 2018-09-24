from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'manager_id', 'role_id', 'dept_id', 'username', 'first_name', 'last_name', 'gender', 'dob',
                  'email', 'fathername', 'mobileno', 'groups', 'password')


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'title', 'project_id')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title')


class UserTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTeam
        fields = ('id', 'user', 'team', 'joining')


class UserProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProject
        fields = ('id', 'user', 'project')


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ('url', 'id', 'name', 'created_date', 'location', 'phoneno')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Departments
        fields = ('url', 'id', 'name', 'created_date', 'companyid', 'phoneno', 'dept_head', 'desc')


class DesignationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Designation
        fields = ('id', 'name', 'desc', 'dept_id', 'isActive')


class LeaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Leaves
        fields = ('url', 'id', 'start_date', 'end_date', 'isapprove', 'isSick', 'ispaid', 'isCasual', 'emp_id')


class AttendanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Attendance
        fields = ('id', 'date', 'emp_id', 'status', 'leave')


class SalarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Salary
        fields = ('id', 'date', 'emp_id', 'basic_salary', 'isPaid')


class DesigDeptSerializer(serializers.ModelSerializer):

    class Meta:
        model = DesigDept
        fields = ('id', 'isActive', 'dept_id', 'role_id', 'start_date', 'end_date')


class CompanyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyPolicy
        fields = ('id', 'role_id', 'medical_fund', 'provident_fund', 'no_sick', 'no_casual')




