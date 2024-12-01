from django.urls import path

from .views import MovieListView, GenreListView, MovieDetalsView

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("genres/", GenreListView.as_view()),
    path("movies/<str:slug>/", MovieDetalsView.as_view())
]