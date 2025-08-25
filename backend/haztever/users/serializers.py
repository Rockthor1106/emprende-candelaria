from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    
    def save(self, request):
    
        user = super().save(request)
        
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        
        user.save()
        
        return user
        
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('first_name', 'last_name')
        read_only_fields = UserDetailsSerializer.Meta.read_only_fields + ('username',)
class CustomLoginSerializer(serializers.Serializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})
    
    def authenticate(self, **kwargs):
        return super().authenticate(email=kwargs['email'], password=kwargs['password'])
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            attrs['username'] = email
            return super().validate(attrs)
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")