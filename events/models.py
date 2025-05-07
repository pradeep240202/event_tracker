from django.db import models

class Event(models.Model):
    type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.source
