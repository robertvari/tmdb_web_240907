from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # this is our API endpoint
    path("api/tmdb/", include("tmdb_database.urls"))
]