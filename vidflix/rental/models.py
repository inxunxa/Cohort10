from django.db import models
from django.utils import timezone

# Create your models here.

"""
    Run  migrations everytime you modify models

    - python manage.py makemigrations
    - python manage.py migrate
"""


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    release_year = models.IntegerField()
    price = models.FloatField()
    image_url = models.TextField()
    description = models.TextField()
    release_date = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + str(self.release_year) + " | " + str(self.price)
