from rest_framework import viewsets

from productservice.productmanager.models import Produkt
from productservice.productmanager.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProductSerializer
