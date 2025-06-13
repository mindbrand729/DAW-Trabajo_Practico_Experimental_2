from django.db import models

# Create your models here.
class Supplier(models.Model):
    name_supplier = models.CharField(max_length=200, blank=False, null=False)
    description_supplier = models.TextField(blank=False, null=False)
    phone_supplier = models.CharField(max_length=20, blank=False, null=False)
    country_supplier = models.CharField(max_length=100, blank=False, null=False)
    mail_supplier = models.EmailField(blank=False, null=False)
    address_supplier = models.TextField(blank=False, null=False)