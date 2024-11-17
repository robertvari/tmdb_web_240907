from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    homepage = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"