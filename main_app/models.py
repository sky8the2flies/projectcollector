from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    url = models.CharField(max_length=250)
    technologies = ArrayField(models.CharField(max_length=25))
    def __str__(self):
        return self.name