# Generated by Django 5.2.3 on 2025-06-19 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_company',
        ),
    ]
