from django.db import models

from haztever.business.models import BusinessProfile


class Product(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='products')


class ProductPhoto(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='product_photos/')