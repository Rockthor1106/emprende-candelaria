from rest_framework import serializers
from .models import BusinessProfile
from .models import BusinessCategory

class BusinessProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessProfile
        
        fields = [
            'id',
            'business_name',
            'logo',
            'banner',
            'category',
            'whatsapp',
            'social_networks',
        ]
        
        read_only_fields = ['user']
        
class BusinessCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessCategory
        
        fields = [
            'id',
            'name',
        ]