# Generated by Django 2.1.1 on 2018-09-18 08:56

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('payroll', '0003_auto_20180917_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]