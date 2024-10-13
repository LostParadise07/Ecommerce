from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/',default='brands/default-logo.png')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')  
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subcategories/',default='brands/default-logo.png') 

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', default='brands/default-logo.png')
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name='products')  
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='products/',default='brands/default-logo.png')  
    available = models.BooleanField(default=True)  
    url_to_brand_page = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
