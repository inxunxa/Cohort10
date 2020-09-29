from django.contrib import admin
from .models import Movie, Genre

# Register your models here.


class MovieTemplate(admin.ModelAdmin):
    list_display = ("id", "title", "release_date", "price")
    list_display_links = ("id", "title")
    # fields = ("genre", "release_year",  "title", "director",
    #          "description", "image_url", "release_date")
    # exclude = ("price",)


class GenreTemplate(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(Movie, MovieTemplate)
admin.site.register(Genre, GenreTemplate)
