# to create migrations for DB changes: ./manage.py makemigrations productmanager
import requests
from django.db import models
from rest_framework import status
from rest_framework.exceptions import NotFound

from . import settings
from .exceptions import CategoryServiceUnavailable


class Product(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category_id = models.PositiveBigIntegerField(null=True, blank=True)

    @property
    def category(self) -> str:
        category_service_url: str = f'{settings.CATEGORY_SERVICE_SCHEME}://{settings.CATEGORY_SERVICE_HOST}:{settings.CATEGORY_SERVICE_PORT}/category/{self.category_id}'

        try:
            r: requests.Response = requests.get(category_service_url)
        except requests.ConnectionError:
            raise CategoryServiceUnavailable()

        if r.status_code == status.HTTP_404_NOT_FOUND or r.text == "":  # Yes, category service doesn't return a valid status code
            raise NotFound(detail='Category not found')

        response = r.json()

        return response.get('name')

    # TODO: Funktionen implementieren category immer als name zurückgeben
    def get_product_by_name(self, name):  # tdb
        print('')

    def get_products_for_search_values(self, search_value, search_min_price, search_max_price):  # tbd
        print('')

    def delete_products_by_category_id(self, category_id):  # tbd
        print('')

        """
        public List<Product> getProducts();

        public Product getProductById(int id);

        public Product getProductByName(String name);

        public int addProduct(String name, double price, int categoryId, String details);

        public List<Product> getProductsForSearchValues(String searchValue, Double searchMinPrice, Double searchMaxPrice);

        public boolean deleteProductsByCategoryId(int categoryId);

        public void deleteProductById(int id);
        """

    def __str__(self):
        return self.name
