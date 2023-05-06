from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'details', 'price']

    def retrieve(self, request, *args, **kwargs):
        """
        Lookup per ID or per product name is possible
        """
        return super().retrieve(self, request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        lookup_value = self.kwargs[self.lookup_field]
        obj = None
        try:
            obj = queryset.get(pk=int(lookup_value))
        except ValueError:
            obj = queryset.get(name=lookup_value)

        if obj is None:
            raise Http404

        self.check_object_permissions(self.request, obj)
        return obj
