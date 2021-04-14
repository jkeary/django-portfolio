from django.shortcuts import render

from .models import ProjectType

def home(request):
    project_types = ProjectType.objects
    return render(request, 'projects/home.html', {'project_types': project_types})