from django.contrib import admin
from .models import TrackHub, Track, SuperTrack

admin.site.register(Track)
admin.site.register(TrackHub)
admin.site.register(SuperTrack)
