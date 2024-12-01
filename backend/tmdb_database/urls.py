from django.urls import path

from .views import MovieListView, GenreListView

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("genres/", GenreListView.as_view())
]