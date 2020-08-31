from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
