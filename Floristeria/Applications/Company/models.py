from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
import os

def validar_extension_imagen(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpe', '.jpg', '.jpeg', '.gif', '.png', '.bmp', '.ico', '.svg', 'svgz', '.tif', '.tiff', '.ai', '.drw', '.pct', '.psp', '.xcf', '.psd', '.raw', '.webp', '.heic']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Solo se permiten imágenes con extensión: .jpe, .jpg, .jpeg, .gif, .png, .bmp, .ico, .svg, svgz, .tif, .tiff, .ai, .drw, .pct, .psp, .xcf, .psd, .raw, .webp, .heic')

def validar_tamano_imagen(value):
    filesize = value.file.size
    max_size = 2 * 1024 * 1024
    if filesize > max_size:
        raise ValidationError("La imagen no puede ser mayor a 2MB.")


# Create your models here.
class Company(models.Model):
    name_company = models.CharField(max_length=100, validators=[MinLengthValidator(3), RegexValidator(regex=r'^[A-Za-z0-9\s\.\-&]+$')], blank=False, null=False)
    address_company = models.CharField(max_length=150, validators=[MinLengthValidator(5)], blank=False, null=False)
    mission_company = models.TextField(validators=[MinLengthValidator(10)], blank=False, null=False)
    vision_company = models.TextField(validators=[MinLengthValidator(10)], blank=False, null=False)
    founding_company = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(datetime.now().year)], blank=False, null=False)
    ruc_company = models.CharField(max_length=13, validators=[RegexValidator(regex=r'^\d{13}$')], unique=True, blank=False, null=False)
    imagen_company = models.ImageField(upload_to='company/', blank=True, null=True, validators=[validar_extension_imagen, validar_tamano_imagen])