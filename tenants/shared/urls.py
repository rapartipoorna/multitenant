from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from shared import views
app_name='shared'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="shared/index.html")),


]
