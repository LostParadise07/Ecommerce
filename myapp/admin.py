from django.contrib import admin
from .models import Category, Brand, Product, Subcategory

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Product)
