from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Gender:
    Male = 'M'
    Female = 'F'
    Other = 'O'
    choices = (
        (Male, 'Male'),
        (Female, 'Female'),
        (Other, 'Other'),
    )


class State:
    yes = 'Y'
    no = 'N'
    choices = (
        (yes, 'yes'),
        (no, 'no'),
    )


class Status:
    Present = 'P'
    Absent = 'A'
    Holiday = 'H'
    choices = (
        (Present, 'Present'),
        (Absent, 'Absent'),
        (Holiday, 'Holiday'),
    )


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField()
    created_date = models.DateField(
            default=timezone.now)
    phoneno = models.BigIntegerField()

    class Meta:
        db_table = 'Company'
        verbose_name_plural = "Company"

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_date = models.DateField()
    phoneno = models.BigIntegerField()
    companyid = models.ForeignKey('Company', on_delete=models.CASCADE)
    dept_head = models.ForeignKey('User', blank=True, null=True, on_delete=None, default=None)

    class Meta:
        db_table = 'Departments'
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    dept_id = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'Designations'
        verbose_name_plural = "Designations"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Project'
        verbose_name_plural = "Project"

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=20)
    project_id = models.ForeignKey('Project', on_delete=None, null=True, blank=True)

    class Meta:
        db_table = 'Team'
        verbose_name_plural = "Team"

    def __str__(self):
        return self.title


class UserTeam(models.Model):
    team = models.ForeignKey('Team', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    joining = models.DateField()

    class Meta:
        db_table = 'UserTeam'
        verbose_name_plural = "UserTeam"

    def __str__(self):
        return str(self.user) + ' ' + str(self.team)


class UserProject(models.Model):
    project = models.ForeignKey('Project', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)

    class Meta:
        db_table = 'UserProject'
        verbose_name_plural = "UserProject"

    def __str__(self):
        return str(self.user) + ' ' + str(self.project)


class DesigDept(models.Model):
    desig = models.ForeignKey('Designation', on_delete=models.CASCADE)
    dept = models.ForeignKey('Departments', on_delete=models.CASCADE)
    isActive = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'DesigDept'
        verbose_name_plural = "DesigDept"


class CompanyPolicy(models.Model):
    role_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    provident_fund = models.FloatField()
    no_sick = models.IntegerField()
    no_casual = models.IntegerField()
    medical_fund = models.IntegerField()

    class Meta:
        db_table = 'CompanyPolicy'
        verbose_name_plural = "CompanyPolicy"


class User(AbstractUser):
    fathername = models.CharField(max_length=20, null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(choices=Gender.choices, max_length=1,null=True,blank=True)
    mobileno = models.CharField(max_length=20,null=True,blank=True)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE,null=True, default=None, blank=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=None, default=None)
    designation = models.ForeignKey('Designation', blank=True, on_delete=None, null=True, default=None)

    class Meta:
        db_table = 'User'
        verbose_name_plural = "User"

    def __str__(self):
        return self.username


class Salary(models.Model):
    isPaid = models.CharField(choices=State.choices, max_length=3)
    basic_salary = models.IntegerField()
    date = models.DateField()
    emp_id = models.ForeignKey('User', related_name='Salary', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Salary'
        verbose_name_plural = "Salary"
        ordering = ('date',)

    def __str__(self):
        return self.date.month


class Leaves(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    ispaid = models.BooleanField()
    isapprove = models.BooleanField()
    isSick = models.BooleanField()
    isCasual = models.BooleanField()
    emp_id = models.ForeignKey('User', related_name='Leaves', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Leaves'
        verbose_name_plural = "Leaves"
        ordering = ('start_date', 'end_date')

    def __str__(self):
        return self.start_date.day


class Attendance(models.Model):
    date = models.DateField()
    status = models.CharField(choices=Status.choices, max_length=1, default='A')
    leave = models.ForeignKey('Leaves', on_delete=None,null=True, blank=True, default=None )
    emp_id = models.ForeignKey('User', related_name='Attendance', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Attendance'
        verbose_name_plural = "Attendance"
