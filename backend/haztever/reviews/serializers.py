from rest_framework import serializers

from .models import Review
from .models import ReviewPhoto

class ReviewPhotoSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = ReviewPhoto
        
        fields = [
            'review',
            'photo'
        ]
        
        read_only_fields = ['review']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.photo:
            request = self.context.get('request')
            representation['photo'] = request.build_absolute_uri(instance.photo.url)
            
        return representation

class ReviewSerializer(serializers.ModelSerializer):
    
    photos = ReviewPhotoSerializer(many=True, read_only=True)
     
    class Meta():
        model = Review
        
        fields = [
            'id',
            'message',
            'score',
            'username',
            'email',
            'business',
            'photos',
        ]
        
        read_only_fields = ['business']
    