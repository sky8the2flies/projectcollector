from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'main_app/about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'main_app/projects/index.html', {'projects': projects})

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'main_app/projects/detail.html', {'project': project})