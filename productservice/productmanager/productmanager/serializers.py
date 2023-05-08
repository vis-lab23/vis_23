import requests
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound

from . import exceptions
from . import models
from . import settings


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200, min_length=1, required=True)

    class Meta:
        model = models.Product
        fields = ["name", "details", "price", "category"]

    def create(self, validated_data: dict):
        category_name: str = self.validated_data.get("category")

        category_service_url: str = f"{settings.CATEGORY_SERVICE_SCHEME}://{settings.CATEGORY_SERVICE_HOST}:{settings.CATEGORY_SERVICE_PORT}/category"

        try:
            r: requests.Response = requests.get(
                category_service_url, params={"name": category_name}
            )
        except requests.ConnectionError:
            raise exceptions.CategoryServiceUnavailable()

        if (
            r.status_code == status.HTTP_404_NOT_FOUND or r.text == ""
        ):  # Yes, category service doesn't return a valid status code
            raise NotFound(detail="Category not found")

        response = r.json()

        category_id: str = response.get("id")

        validated_data.pop("category")
        validated_data["category_id"] = category_id

        return super().create(validated_data)
