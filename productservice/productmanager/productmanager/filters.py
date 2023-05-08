from typing import List

from django_filters import rest_framework as filters

from . import models


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = models.Product
        fields: List[str] = []
