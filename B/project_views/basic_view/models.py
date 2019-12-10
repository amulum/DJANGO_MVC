from django.db import models

# Create your models here.
class Blog(models.Model):
    image_path      = models.CharField(blank=False, null=False)
    header          = models.CharField(max_length=300)
    content         = models.CharField(blank-False, null=False)

class Mentor(models.Model):
    image_path      = models.CharField(blank=False, null=False)
    name            = models.CharField(max_length=100)
    experience      = models.CharField(max_length=300)
    quote           = models.CharField(max_length=300)

class Mentee(models.Model):
    image_path      = models.CharField(blank=False, null=False)
    name            = models.CharField(max_length=100)
    quote           = models.CharField(max_length=300)