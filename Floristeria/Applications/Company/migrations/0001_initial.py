# Generated by Django 5.2.3 on 2025-06-25 20:34

import Applications.Company.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(regex='^[A-Za-z0-9\\s\\.\\-&]+$')])),
                ('address_company', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5)])),
                ('mission_company', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('vision_company', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('founding_company', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2025)])),
                ('ruc_company', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{13}$')])),
                ('imagen_company', models.ImageField(blank=True, null=True, upload_to='company/', validators=[Applications.Company.models.validar_extension_imagen, Applications.Company.models.validar_tamano_imagen])),
            ],
        ),
    ]
