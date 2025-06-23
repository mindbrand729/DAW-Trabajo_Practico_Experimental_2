from django.db import models

# Create your models here.
class Supplier(models.Model):
    name_supplier = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre del Proveedor")
    phone_supplier = models.CharField(max_length=20, blank=False, null=False, verbose_name="Teléfono")
    country_supplier = models.CharField(max_length=100, blank=False, null=False, verbose_name="País")
    mail_supplier = models.EmailField(blank=False, null=False, verbose_name="Correo Electrónico")

