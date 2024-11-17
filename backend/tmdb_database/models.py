from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class SortItem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    poster_path = models.ImageField(blank=True)
    backdrop_path = models.ImageField(blank=True)
    vote_average = models.FloatField(blank=True, default=0)
    popularity = models.FloatField(blank=True, default=0)
    overview = models.TextField(max_length=2000, blank=True)
    language = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title