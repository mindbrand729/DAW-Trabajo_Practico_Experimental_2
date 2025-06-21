from django.db import models

# Create your models here.
class Supplier(models.Model):
    name_supplier = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre del Proveedor")
    description_supplier = models.TextField(blank=False, null=False, verbose_name="Descripción")
    phone_supplier = models.CharField(max_length=20, blank=False, null=False, verbose_name="Teléfono")
    country_supplier = models.CharField(max_length=100, blank=False, null=False, verbose_name="País")
    mail_supplier = models.EmailField(blank=False, null=False, verbose_name="Correo Electrónico")
    address_supplier = models.TextField(blank=False, null=False, verbose_name="Dirección")
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.name_supplier