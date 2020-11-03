from rest_framework import serializers
from shared.models import Client
from django.contrib.auth.models import User
class tenant_data_serializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
