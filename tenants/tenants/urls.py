from django.contrib import admin
from django.urls import path,include
from shared import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shared.urls',namespace='shared')),
    path('api/',include('tenant_api.urls',namespace='tenant_api')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('accounts/', views.schema_view.as_view()),
]
