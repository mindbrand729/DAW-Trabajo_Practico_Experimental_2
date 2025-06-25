from django.db import models
from Applications.Supplier.models import Supplier
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
import os

def validar_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpe', '.jpg', '.jpeg', '.gif', '.png', '.bmp', '.ico', '.svg', 'svgz', '.tif', '.tiff', '.ai', '.drw', '.pct', '.psp', '.xcf', '.psd', '.raw', '.webp', '.heic']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Solo se permiten imágenes con extensión: .jpe, .jpg, .jpeg, .gif, .png, .bmp, .ico, .svg, svgz, .tif, .tiff, .ai, .drw, .pct, .psp, .xcf, .psd, .raw, .webp, .heic')

def validar_tamano(value):
    filesize = value.file.size
    max_size = 2 * 1024 * 1024
    if filesize > max_size:
        raise ValidationError("La imagen no puede ser mayor a 2MB.")

# Create your models here.
class Products(models.Model):
    IVA_CHOICES = [
        (15, '15%'),
        (0, '0%'),
    ]

    name_products = models.CharField(max_length=200, validators=[MinLengthValidator(3), RegexValidator(regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+$"
)], blank=False, null=False)
    description_products = models.TextField(validators=[MinLengthValidator(10)], blank=False, null=False)
    price_products = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=False, null=False)
    iva_products = models.IntegerField(choices=IVA_CHOICES, blank=False, null=False)
    imagen_products = models.ImageField(upload_to='products/', blank=True, null=True, validators=[validar_extension, validar_tamano])