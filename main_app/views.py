from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Project
from .forms import TimelineForm

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'main_app/projects/index.html', {'projects': projects})

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    timeline_form = TimelineForm()
    return render(request, 'main_app/projects/detail.html', {
        'project': project, 'timeline_form': timeline_form
    })

def add_timeline(request, project_id):
    form = TimelineForm(request.POST)
    if form.is_valid():
        new_timeline = form.save(commit=False)
        new_timeline.project_id = project_id
        new_timeline.save()
    return redirect('detail', project_id=project_id)

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'