
from rest_framework import routers, serializers, viewsets
from app.models import Usercustome,UserProfile
  
    

class UsercustomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercustome
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
    def create(self, validated_data):
        user = Usercustome(
            # id=validated_data['id'],
            username=validated_data['username'],
            user_role=validated_data['user_role'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"