from django.db import models

# Create your models here.
class Employee(models.Model):
    name_employee = models.CharField(max_length=100)
    surname_employee = models.CharField(max_length=100)
    mail_employee = models.EmailField()
    card_employee = models.CharField(max_length=20, unique=True)
    code_employee = models.CharField(max_length=20, unique=True)
    imagen_employee = models.ImageField(upload_to='trabajadores/', blank=True, null=True)

    def __str__(self):
        return f"{self.name_employee} {self.surname_employee}"