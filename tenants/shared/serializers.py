from rest_framework import serializers
from shared.models import Client
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
user=get_user_model()
class tenant_data_serializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class UsercreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=user
        fields = ('id', 'email', 'username', 'phone', 'password')
        # fields = ('id','email','username','password')



