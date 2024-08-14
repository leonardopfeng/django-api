from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    tax = models.FloatField()
    code = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField()
    promotion = models.BooleanField()

    def __str__(self):
        return self.name
