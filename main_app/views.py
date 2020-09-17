from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Project, Author
from .forms import TimelineForm

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    authors_notin_project = Author.objects.exclude(id__in=project.authors.all().values_list('id'))
    timeline_form = TimelineForm()
    return render(request, 'main_app/projects/detail.html', {
        'project': project, 
        'timeline_form': timeline_form,
        'authors': authors_notin_project
    })

def add_timeline(request, project_id):
    form = TimelineForm(request.POST)
    if form.is_valid():
        new_timeline = form.save(commit=False)
        new_timeline.project_id = project_id
        new_timeline.save()
    return redirect('detail', project_id=project_id)

class SearchResultsView(ListView):
    model = Project
    template_name = 'main_app/projects/index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Project.objects.all()
        return Project.objects.filter(
            Q(name__icontains=query) | 
            Q(technologies__icontains=query) |
            Q(description__icontains=query)
        )

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'

class AuthorSearchResultsView(ListView):
    model = Author
    template_name = 'main_app/authors/author_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Author.objects.all()
        return Author.objects.filter(
            Q(name__icontains=query) | 
            Q(git_user__icontains=query) |
            Q(description__icontains=query)
        )

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'main_app/authors/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'main_app/authors/author_form.html'

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'main_app/authors/author_form.html'

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/authors/'
    template_name = 'main_app/authors/author_confirm_delete.html'

def assoc_author(request, project_id, author_id):
    Project.objects.get(id=project_id).authors.add(author_id)
    return redirect('detail', project_id=project_id)