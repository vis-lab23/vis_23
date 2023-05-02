from django.db import models


class Produkt(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2)
    category_id = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
