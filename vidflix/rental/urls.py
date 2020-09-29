from django.urls import path
from . import views

# collection of valid router for rental app
urlpatterns = [
    path('', views.index, name="root"),
    path('test', views.test, name="test"),
    path('home/something', views.index, name="long"),
    path('about', views.about, name="about"),
    path('catalog', views.catalog, name="catalog"),
    path('catalog2', views.catalog2, name="catalog2"),
    path('details/<int:id>', views.details, name="details"),
]
