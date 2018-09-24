# Generated by Django 2.1.1 on 2018-09-17 11:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fathername', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('H', 'Holiday')], default='A', max_length=1)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attendance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'db_table': 'Attendance',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('phoneno', models.BigIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Company',
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='CompanyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provident_fund', models.FloatField()),
                ('no_sick', models.IntegerField()),
                ('no_casual', models.IntegerField()),
                ('medical_fund', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'CompanyPolicy',
                'db_table': 'CompanyPolicy',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('created_date', models.DateField()),
                ('phoneno', models.BigIntegerField()),
                ('companyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Company')),
                ('dept_head', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'db_table': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ispaid', models.BooleanField()),
                ('isapprove', models.BooleanField()),
                ('isSick', models.BooleanField()),
                ('isCasual', models.BooleanField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Leaves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Leaves',
                'db_table': 'Leaves',
                'ordering': ('start_date', 'end_date'),
            },
        ),
        migrations.CreateModel(
            name='RoleDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Departments')),
            ],
            options={
                'verbose_name_plural': 'RoleDept',
                'db_table': 'RoleDept',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(null=True)),
                ('isActive', models.BooleanField(default=False)),
                ('dept_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payroll.Departments')),
            ],
            options={
                'verbose_name_plural': 'Roles',
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPaid', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=3)),
                ('basic_salary', models.IntegerField()),
                ('date', models.DateField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Salary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Salary',
                'db_table': 'Salary',
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='roledept',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Roles'),
        ),
        migrations.AddField(
            model_name='companypolicy',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Roles'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='leave',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=None, to='payroll.Leaves'),
        ),
        migrations.AddField(
            model_name='user',
            name='dept_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.Departments'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='manager_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=None, to='payroll.Roles'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
