from django.urls import path

from .views import MovieListView, GenreListView, SortListView

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("genres/", GenreListView.as_view()),
    path("sort-list/", SortListView.as_view())
]