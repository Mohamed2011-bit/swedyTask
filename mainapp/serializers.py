from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializerList(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email', 'user_status', 'first_name', 'last_name' )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email', 'user_status', 'first_name', 'last_name' , 'password')
        extra_kwargs = {"password": {"error_messages": {"required": "Please enter password"}}}