from django.db import models
from django.utils import timezone

class Basic_data(models.Model):
    artist_name = models.CharField(max_length=20)#地名
    artist_track = models.CharField(max_length=20)
    artist_audio = models.URLField()
    artist_url = models.URLField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    writer = models.CharField(max_length=10)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.artist_name
