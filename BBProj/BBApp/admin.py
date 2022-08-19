from django.contrib import admin
from .models import Product, BarrowProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(BarrowProduct)