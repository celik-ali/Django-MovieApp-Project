from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path('home', views.home, name="homex"),
    path("movies", views.movies, name="movies"),
    path("movies/<int:id>", views.movieDetails, name="details")
]