from django.db import models

# Create your models here.
class Company(models.Model):
    name_company = models.CharField(max_length=100, blank=False, null=False)
    address_company = models.CharField(max_length=100, blank=False, null=False)
    mission_company = models.TextField(blank=False, null=False)
    vision_company = models.TextField(blank=False, null=False)
    founding_company = models.PositiveIntegerField(blank=False, null=False)
    ruc_company = models.CharField(max_length=13, unique=True, blank=False, null=False)
    imagen_company = models.ImageField(upload_to='empresas/', blank=True, null=True)