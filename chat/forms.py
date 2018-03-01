from django import forms
from .models import Basic_data

class PostForm(forms.ModelForm):

    class Meta:
        model = Basic_data
        fields = ("artist_name", "artist_track", "artist_audio", "artist_url", "writer")
