from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'available', 'created']
    list_display_links = ['id', 'name']
    list_filter = ['price', 'available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ['name']}