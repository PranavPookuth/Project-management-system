from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateView.as_view(), name='project-detail'),
    path('projects/<int:pk>/upload-image/', ProjectImageUploadView.as_view(), name='project-image-upload'),
    path('projects/delete/', ProjectDeleteMultipleView.as_view(), name='project-soft-delete'),
    path('projects/<int:pk>/download/', ProjectCSVDownloadView.as_view(), name='project-csv-download'),

    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('projects/<int:project_id>/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
