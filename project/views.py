from django.shortcuts import render, get_object_or_404
from .models import ProjectType, Project

def home(request):
    project_types = ProjectType.objects
    return render(request, 'projects/home.html', {'project_types': project_types})

def listview(request, project_type):
    projects = Project.objects.filter(project_type__in=ProjectType.objects.filter(nav_name=project_type)).order_by('-start_date')
    return render(request, 'projects/list.html', {'projects': projects, 'project_type': project_type, 'project_types': ProjectType.objects.all()})

def projectview(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})