from django.db import models
from json import dumps


class PropertiesKey(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PropertiesValue(models.Model):
    properties_key = models.ForeignKey('PropertiesKey', on_delete=models.CASCADE)
    value = models.JSONField()

    class Meta:
        ordering = ['value']

    def __str__(self):
        return dumps(
            self.value,
            indent=2,
        )


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    img = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField('Category')
    properties = models.ManyToManyField('PropertiesValue')

    class Meta:
        ordering = ['name', 'price']

    def __str__(self):
        return self.name
