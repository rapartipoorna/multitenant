from django.contrib import admin
from django.urls import path
from . views import create_tenant

app_name='tenant_api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',create_tenant.as_view(),name='listcreate')


]
