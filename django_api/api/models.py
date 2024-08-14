from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    code = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
