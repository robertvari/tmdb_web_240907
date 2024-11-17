from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
    discount_price = models.IntegerField(default=0)
    discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name