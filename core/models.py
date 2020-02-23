from django.db import models


class Product(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
