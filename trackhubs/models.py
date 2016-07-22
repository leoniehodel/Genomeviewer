from django.db import models
from genomebrowser.models import Genome

# Create your models here.
class TrackHub(models.Model):
    Genome = models.ForeignKey(Genome, on_delete=models.CASCADE)
    hub_name = models.CharField(max_length=500)
    short_label = models.CharField(max_length=500)
    long_label = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.hub_name


class SuperTrack(models.Model):
    TrackHub = models.ForeignKey(TrackHub, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_label = models.CharField(max_length=500)
    long_label = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Track(models.Model):
    TrackHub = models.ForeignKey(TrackHub, on_delete=models.CASCADE)
    Supertrack = models.BooleanField(False)
    name = models.CharField(max_length=500)
    short_label = models.CharField(max_length=500)
    long_label = models.CharField(max_length=1000)
    url = models.CharField(max_length=500)
    track_type = models.CharField(max_length=20)
    color = models.CharField(max_length=500, default='0,0,220')


    def __str__(self):
        return self.name
