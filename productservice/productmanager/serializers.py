from rest_framework import serializers

from productservice.productmanager.models import Produkt


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'
