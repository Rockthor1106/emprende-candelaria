from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    

class BusinessProfile(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='business_logos/')
    banner = models.ImageField(upload_to='business_banners/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='business_profiles')
    whatsapp = models.CharField(max_length=20)
    social_networks = models.JSONField(blank=True, null=True, verbose_name='Secondary social networks')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


