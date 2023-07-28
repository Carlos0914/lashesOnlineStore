from djongo import models
from django.contrib import admin


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    alttext = models.CharField(max_length=30, primary_key=True)


class Product(models.Model):
    identifier = models.CharField(max_length=20)
    name = models.CharField(max_length=60, primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
    images = models.ArrayReferenceField(to=Image, on_delete=models.CASCADE)

    objects = models.DjongoManager()


admin.site.register(Product)
admin.site.register(Image)
