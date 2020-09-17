from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=25)
    git_user = models.CharField(max_length=25)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.id})

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    url = models.CharField(max_length=250)
    technologies = ArrayField(models.CharField(max_length=25))
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})

class Timeline(models.Model):
    date = models.DateField('feature date')
    action = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return f'On {self.date}, {self.action}'
    class Meta:
        ordering = ['-date']