from rest_framework import serializers

from .models import Product
from .models import ProductCategory

class ProductSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category'
        ]
        
        read_only_fields = ['business']
        
class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name'
        ]

