from django.db import models

# Create your models here.
class Employee(models.Model):
    name_employee = models.CharField(max_length=100, blank=False, null=False)
    surname_employee = models.CharField(max_length=100, blank=False, null=False)
    mail_employee = models.EmailField(blank=False, null=False)
    card_employee = models.CharField(max_length=20, unique=True, blank=False, null=False)
    code_employee = models.CharField(max_length=20, unique=True, blank=False, null=False)
    imagen_employee = models.ImageField(upload_to='trabajadores/', blank=True, null=True)

    def __str__(self):
        return f"{self.name_employee} {self.surname_employee}"