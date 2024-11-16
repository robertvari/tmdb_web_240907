from django.contrib import admin
from django.urls import path, include

from tmdb_database.views import MovieListView, NavbarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # this is our API endpoint
    path("api/movies/", MovieListView.as_view()),
    path("api/nav-items/", NavbarView.as_view())
]