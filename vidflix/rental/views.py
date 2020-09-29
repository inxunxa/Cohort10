from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre

# Create your views here.


def index(request):
    return render(request, "index.html", {"title": "Welcome"})


def test(request):
    return HttpResponse("Test page")


def about(request):
    return render(request, "about.html", {"title": "About us"})


def catalog(request):
    all_movies = Movie.objects.all()
    return render(request, "catalog.html", {"title": "SSR Catalog", "movies": all_movies})

def catalog2(request):
    return render(request, "catalog2.html", {"title": "CSR Catalog"})


def details(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "details.html", {"title": "Movie details", "movie": movie})


"""
create details.html
render details.html

send the movie as a variable to html
render the movie in an h1 in the html
"""
