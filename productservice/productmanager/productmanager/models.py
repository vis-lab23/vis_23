from django.contrib.sites import requests
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category_id = models.PositiveBigIntegerField()

    # TODO: Funktionen implementieren category immer als name zurückgeben
    def get_product_by_name(self, name): #tdb
        print('')

    def get_products(self, name): #tdb
        print('')

    def add_product(self, name, price, category_id, details): #tbd categorie
        print('')

    def get_products_for_search_values(self, search_value, search_min_price, search_max_price): #tbd
        print('')

    def delete_products_by_category_id(self, category_id): #tbd
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
