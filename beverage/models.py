from django.db import models

# Create your models here.


class Beverage(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    picture = models.CharField(max_length=2083)
