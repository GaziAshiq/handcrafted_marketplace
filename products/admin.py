from django.contrib import admin
from .models import Product


# Register your models here.
# read models.py and create admin interface for Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'quantity', 'image')
    list_filter = ('name', 'slug', 'price', 'quantity', 'image')
    search_fields = ('name', 'slug', 'price', 'quantity', 'image')
    # prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'slug', 'price', 'quantity', 'image')
    list_per_page = 10
