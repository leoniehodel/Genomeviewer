from django import forms
from .models import TrackHub, Track


class TrackHubForm(forms.ModelForm):

    class Meta:
        model = TrackHub
        fields = ['Genome', 'hub_name', 'long_label', 'short_label', 'email']


class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = ['TrackHub', 'Supertrack', 'name', 'long_label', 'short_label', 'url', 'track_type', 'color']