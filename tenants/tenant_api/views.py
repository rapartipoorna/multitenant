from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from shared.models import Client
from .serializer import tenant_data_serializer


# Create your views here.
class create_tenant(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = tenant_data_serializer
