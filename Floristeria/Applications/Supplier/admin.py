from django.contrib import admin
from .models import Supplier
# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Supplier, SupplierAdmin)

