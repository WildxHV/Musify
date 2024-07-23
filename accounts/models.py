from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pic/', blank=True)
    def __str__(self):
        return self.user.username
    

class Song(models.Model):
    title = models.CharField(max_length= 100)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    def __str__(self):
        return self.title
    
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.name