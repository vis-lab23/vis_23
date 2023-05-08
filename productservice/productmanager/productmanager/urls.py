from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views

router = DefaultRouter()
router.register(r"products", views.ProductByIDViewSet, basename="products-by-id")
router.register(r"products", views.ProductByNameViewSet, basename="products-by-name")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "openapi/",
        get_schema_view(title="Product Service", version="1.0.0"),
        name="openapi-schema",
    ),
    path(
        "openapi-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
