from django.shortcuts import render, get_object_or_404

from .models import ProjectType, Project

def home(request):
    project_types = ProjectType.objects
    return render(request, 'projects/home.html', {'project_types': project_types})

def listview(request, project_type):
    projects = Project.objects.filter(project_type=project_type)
    return render(request, 'projects/list.html', {'projects': projects})

def projectview(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})