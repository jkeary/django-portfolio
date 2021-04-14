from django.db import models
from django.contrib import admin
from datetime import date
from tinymce.models import HTMLField

# Sound Designer would be the job title, Sound woild be the nav bar name.
# PROJECT_TYPE_CHOICES = [
    #     (SOUND, 'Sound Designer'),
    #     (CODE, 'Software Engineer'),
    #     (MUSIC, 'Musician'),
    #     (VIDEO, 'Videographer'),
    # ]
class ProjectType(models.Model):
    job_title = models.CharField(max_length=100)
    nav_name = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

# Projects can be jobs or individual projects that I worked on.
class Project(models.Model):
    title = models.CharField(max_length=250)

    project_type = models.ManyToManyField(ProjectType)
    primary_image = models.ImageField(upload_to='images/')

    # If theres no summary the get summary method could just take the first 1000 chars of the detail.
    summary = HTMLField(max_length=1000, blank=True)
    
    # If you want more than a summary, create a template with the name of the project 
    detail = HTMLField(blank=True, max_length=100000)
    external_link = models.URLField(blank=True)
    template = models.CharField(max_length=100, blank=True)

    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)