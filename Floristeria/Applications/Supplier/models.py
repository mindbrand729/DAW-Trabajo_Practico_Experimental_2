from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Supplier(models.Model):
    name_supplier = models.CharField(max_length=200, validators=[MinLengthValidator(3), RegexValidator(regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+$"
)], blank=False, null=False)
    description_supplier = models.TextField(validators=[MinLengthValidator(10)], blank=False, null=False, verbose_name="Descripción")
    phone_supplier = PhoneNumberField(blank=False, null=False, unique=True, error_messages={'unique': "Este número ya está registrado."})
    country_supplier = models.CharField(max_length=100, validators=[MinLengthValidator(3), RegexValidator(regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+$"
)], blank=False, null=False, verbose_name="País")
    mail_supplier = models.EmailField(blank=False, null=False, unique=True, error_messages={'unique': "Este correo ya está registrado."})
    address_supplier = models.CharField(max_length=150, validators=[MinLengthValidator(5), RegexValidator(regex=r"^(?=.*[A-Za-zÁÉÍÓÚáéíóúÑñ])[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s.,'\-#°/]+$")], blank=False, null=False)
