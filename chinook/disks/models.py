from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.artist_name
   
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.album_title
    
class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.IntegerField(default=0)
    def __str__(self):
        return self.track_name
    

