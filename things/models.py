from django.db import models
import datetime

class ThingTypes(models.TextChoices):
    PHYSICAL = '1', 'Physical'
    DIGITAL = '2', 'Digital'
    MENTAL = '3', 'Mental'

class Thing(models.Model):
  title = models.TextField()
  done = models.BooleanField()
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  doneOn = models.DateTimeField(null=True, blank=True)