from rest_framework import serializers

from .models import Product
from .models import ProductCategory
from .models import ProductPhoto

class ProductPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPhoto
        fields = [
            'id',
            'photo'
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.photo:
            request = self.context.get('request')
            representation['photo'] = request.build_absolute_uri(instance.photo.url)
            
        return representation

class ProductSerializer(serializers.ModelSerializer):
        
    photos = ProductPhotoSerializer(many=True, read_only=True)    
        
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'photos',
        ]
        
        read_only_fields = ['business']
        
class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name'
        ]


