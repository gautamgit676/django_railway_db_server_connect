
from rest_framework import routers, serializers, viewsets
from app.models import Usercustome
  
    

class UsercustomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercustome
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Usercustome.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        return user