from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        
        model = User
        fields = ('id', 'password', 'username', 'email', 'nickname', 'join_date')
    
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}

            }
        }

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'password')

    