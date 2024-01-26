from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateTimeField(auto_now_add=True)
    album_rating = models.IntegerField()

    def __str__(self):
        return self.name
    