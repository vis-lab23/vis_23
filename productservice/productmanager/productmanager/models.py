# to create migrations for DB changes: ./manage.py makemigrations productmanager

import requests
from django.db import models
from rest_framework import status
from rest_framework.exceptions import NotFound

from . import exceptions
from . import settings


class Product(models.Model):
    name: models.CharField = models.CharField(max_length=200, unique=True)
    details: models.CharField = models.CharField(max_length=255)
    price: models.DecimalField = models.DecimalField(decimal_places=2, max_digits=10)
    category_id: models.PositiveBigIntegerField = models.PositiveBigIntegerField(
        null=True, blank=True
    )

    @property
    def category(self) -> str:
        category_service_url: str = f"{settings.CATEGORY_SERVICE_SCHEME}://{settings.CATEGORY_SERVICE_HOST}:{settings.CATEGORY_SERVICE_PORT}/category/{self.category_id}"

        try:
            r: requests.Response = requests.get(category_service_url)
        except requests.ConnectionError:
            raise exceptions.CategoryServiceUnavailable()

        if (
            r.status_code == status.HTTP_404_NOT_FOUND or r.text == ""
        ):  # Yes, category service doesn't return a valid status code
            raise NotFound(detail="Category not found")

        response = r.json()

        return response.get("name")

    def __str__(self):
        return self.name
