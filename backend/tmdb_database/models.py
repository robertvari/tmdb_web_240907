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
    poster_path = models.ImageField()
    backdrop_path = models.ImageField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    overview = models.TextField(max_length=2000)
    language = models.CharField(max_length=200)
