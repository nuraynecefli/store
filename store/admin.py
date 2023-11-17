from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock')
    prepopulated_fields = {'slug': ('product_name',)}

