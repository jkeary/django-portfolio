from django.db import models
from tinymce.models import HTMLField

# Projects can be jobs or individual projects that I worked on.
class Project(models.Model):
    # define project types 
    SOUND = 'SOUND'
    CODE = 'CODE'
    MUSIC = 'MUSIC'
    VIDEO = 'VIDEO'
    
    PROJECT_TYPE_CHOICES = [
        (SOUND, 'Sound Designer'),
        (CODE, 'Software Engineer'),
        (MUSIC, 'Musician'),
        (VIDEO, 'Videographer'),
    ]
    project_type = models.CharField(
        choices=PROJECT_TYPE_CHOICES,
        default=CODE,
        max_length=100,
    )

    primary_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    # If theres no summary the get summary method could just take the first 1000 chars of the detail.
    summary = HTMLField(max_length=1000, blank=True)
    
    # If you want more than a summary, create a template with the name of the project 
    detail = HTMLField(blank=True, max_length=100000)
    template = models.TextField(max_length=100, blank=True)


