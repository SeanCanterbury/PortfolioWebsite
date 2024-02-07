from django.db import models

# Create your models here.

class Project( models.Model):
    title = models.CharField(max_length=100)
    shortDescription = models.TextField(null=True, blank=True)
    description = models.TextField()
    technology = models.CharField(max_length=40)
    image = models.FileField(upload_to='project_images/',blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title 
