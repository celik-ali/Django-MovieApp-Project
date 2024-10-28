from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    film_adi = models.CharField(max_length=100)
    film_detay = models.TextField()
    film_image = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)