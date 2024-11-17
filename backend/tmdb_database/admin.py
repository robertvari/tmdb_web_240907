from django.contrib import admin

from .models import Genre, SortItem, Movie

admin.site.register(Genre)
admin.site.register(SortItem)
admin.site.register(Movie)