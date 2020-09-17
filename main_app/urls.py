from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.SearchResultsView.as_view(), name='search_results'),
    path('projects/create', views.ProjectCreate.as_view(), name='project_create'),
    path('projects/<int:project_id>', views.projects_detail, name='detail'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:project_id>/add_timeline', views.add_timeline, name='add_timeline'),
]