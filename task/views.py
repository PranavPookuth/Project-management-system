from django.shortcuts import render
from rest_framework import generics, permissions, filters, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
import csv
# Create your views here.

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(is_deleted=False).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectImageUploadView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

class ProjectDeleteMultipleView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        Project.objects.filter(id__in=ids).update(is_deleted=True)
        return Response({'message': 'Projects soft-deleted'}, status=status.HTTP_200_OK)

class ProjectCSVDownloadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="project_{project.id}.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Description', 'Start Date', 'End Date', 'Duration'])
        writer.writerow([project.name, project.description, project.start_date, project.end_date, project.duration])
        return response

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_id'])

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs['project_id'])

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_id'])
