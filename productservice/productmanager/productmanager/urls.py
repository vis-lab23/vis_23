from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(title="Product Service", version="1.0.0"), name='openapi-schema'),
]
