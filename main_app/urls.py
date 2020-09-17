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
    path('projects/<int:project_id>/assoc_author/<int:author_id>/', views.assoc_author, name="assoc_author"),
    path('authors/', views.AuthorSearchResultsView.as_view(), name='author_search_results'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    #author_search_results
    #author_create
]