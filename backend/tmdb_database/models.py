from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os, shutil
from PIL import Image

def get_media_path(instance, filename):
    return f"{slugify(instance.title)}/{filename}"

class Genre(models.Model):
    name = models.CharField(max_length=200)
    tmdb_id = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    poster_path = models.ImageField(blank=True, upload_to=get_media_path)
    backdrop_path = models.ImageField(blank=True, upload_to=get_media_path)
    vote_average = models.FloatField(blank=True, default=0)
    popularity = models.FloatField(blank=True, default=0)
    overview = models.TextField(max_length=2000, blank=True)
    language = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize/convert poster
        # if not self.poster_path:
        #     return

        # image_path = self.poster_path.path
        # img = Image.open(image_path)

        # if img.size[0] > 300 or img.size[1] > 300:
        #     img.thumbnail((300, 300))
        #     img.save(image_path)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Movie)
def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f"{instance.tmdb_id}-{instance.title}")

@receiver(post_delete, sender=Movie)
def cleanup_folders(sender, instance, **kwargs):
    media_folder = os.path.dirname(instance.poster_path.path)

    if os.path.exists(media_folder):
        shutil.rmtree(media_folder, ignore_errors=True)