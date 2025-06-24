from django.db import models
from Applications.Company.models import Company
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
class Employee(models.Model):
    name_employee = models.CharField(max_length=100, validators=[MinLengthValidator(3), RegexValidator(regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+$"
)], blank=False, null=False)
    surname_employee = models.CharField(max_length=100, validators=[MinLengthValidator(3), RegexValidator(regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+$"
)], blank=False, null=False)
    mail_employee = models.EmailField(blank=False, null=False, unique=True, error_messages={'unique': "Este correo ya está registrado."})
    card_employee = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$')], unique=True, blank=False, null=False, error_messages={'unique': "Esta cédula ya está registrada."})
    code_employee = models.CharField(max_length=10, validators=[RegexValidator(r'^[A-Z0-9\-]{4,10}$', message="El código solo debe contener letras mayúsculas, números y guiones. Debe tener entre 4 y 10 caracteres.")], unique=True, blank=False, null=False, error_messages={'unique': "Este código ya está registrado."})
    imagen_employee = models.ImageField(upload_to='employees/', blank=True, null=True, validators=[validar_extension, validar_tamano])