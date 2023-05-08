from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as FrameworkFilters
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema

from . import exceptions
from . import filters
from . import models
from . import serializers


class ProductByIDViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [FrameworkFilters.SearchFilter, DjangoFilterBackend]
    filterset_class = filters.ProductFilter
    search_fields = ["name", "details", "price"]
    lookup_value_regex = "[0-9]+"

    @action(
        methods=["delete"], detail=False, url_path="category/(?P<category_id>[0-9]+)"
    )
    def category(self, request, pk=None, *args, **kwargs):
        cid = kwargs.get("category_id", None)
        if cid == None:
            raise exceptions.CategoryIDMissing

        qs = self.get_queryset()
        qs.filter(category_id=cid).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductByNameViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    schema = AutoSchema(operation_id_base="ProductByName")
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [FrameworkFilters.SearchFilter]
    search_fields = ["name", "details", "price"]
    lookup_field = "name"
    lookup_value_regex = "[0-9A-Za-z]+"
