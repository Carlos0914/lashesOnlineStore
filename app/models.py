from djongo import models
from django.contrib import admin


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    alttext = models.CharField(max_length=30, primary_key=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
    images = models.ArrayReferenceField(
        to=Image, on_delete=models.CASCADE, related_name="images_id")

    objects = models.DjongoManager()


class Appointment(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    days = models.JSONField()

    class Meta:
        abstract: True


admin.site.register(Product)
admin.site.register(Image)
