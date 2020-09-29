from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from rental.models import Movie, Genre
from tastypie.authorization import Authorization

# Create your models here.
class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        ordering = ['id', 'name']
        filtering = {  
            'id': ALL,
            'name': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization()
    


class MovieResource(ModelResource):
    # load the related attribute Movie => Genre
    genre = fields.ToOneField(GenreResource, 'genre', full=True)
    class Meta:
        queryset = Movie.objects.all()
        resource_name = "movies"
        ordering = ['title', 'release_year', 'price']
        filtering = {
            'title' : ALL,
            'price': ALL,
            'release_year': ALL,
            'genre': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization()


"""

Ordering:
/api/movies/?order_by=price    Asc
/api/movies/?order_by=-price   DESC


Filter:
/api/movies/?price=12  Exact eq
/api/movies/?price__lt=20  Lower than
/api/movies/?price__gt=5   greater than
/api/movies/?title__contains=forest


"""