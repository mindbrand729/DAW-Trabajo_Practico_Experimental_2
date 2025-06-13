from django.db import models
from Applications.Company.models import Company

# Create your models here.
class Employee(models.Model):
    name_employee = models.CharField(max_length=100, blank=False, null=False)
    surname_employee = models.CharField(max_length=100, blank=False, null=False)
    mail_employee = models.EmailField(blank=False, null=False)
    card_employee = models.CharField(max_length=20, unique=True, blank=False, null=False)
    code_employee = models.CharField(max_length=20, unique=True, blank=False, null=False)
    imagen_employee = models.ImageField(upload_to='trabajadores/', blank=True, null=True)
    employee_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee')