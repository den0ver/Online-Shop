from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'available', 'created']
    list_display_links = ['id', 'name']
    list_filter = ['available', 'price', 'created', 'updated']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ['name']}