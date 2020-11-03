from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializers import tenant_data_serializer,admin_serializer
from rest_framework.response import Response
from shared.models import Client
from rest_framework import status
from tenant_schemas.utils import schema_context


# Create your views here.
class first_view(APIView):
    # queryset = Client.objects.all()
    # serializer_class = tenant_data_serializer

    def get(self,request):
        qs=Client.objects.all()
        serializer = tenant_data_serializer(qs,many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer=tenant_data_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # with schema_context(serializer.data.get('schema_name')):
        #
        #     serializer=admin_serializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        # User.objects.create_superuser('poorna121', 'admin@example.com', 'pass')
        #         s = Product(name='shoes', description='very good item', stock='3')
        #         s.save()
        return Response(status=status.HTTP_201_CREATED)
        # return HttpResponseRedirect("/accounts")



class schema_view(APIView):
    def get(self,request):
        return Response(template_name='inout/profile.html')

