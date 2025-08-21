from django.db import models

from haztever.business.models import BusinessProfile


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    business = models.ForeignKey(BusinessProfile, related_name='product_categories', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} (de {self.business.business_name})'

class Product(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')


class ProductPhoto(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='product_photos/')