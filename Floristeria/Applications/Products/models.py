from django.db import models
from Applications.Supplier.models import Supplier

# Create your models here.
class Products(models.Model):
    IVA_CHOICES = [
        (15, '15%'),
        (0, '0%'),
    ]

    name_products = models.CharField(max_length=200, blank=False, null=False)
    description_products = models.TextField(blank=False, null=False)
    price_products = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    iva_products = models.IntegerField(choices=IVA_CHOICES, blank=False, null=False)
    imagen_products = models.ImageField(upload_to='productos/', blank=True, null=True)
    proveedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)