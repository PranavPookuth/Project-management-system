from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.ReadOnlyField(source='project.id')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['project']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['created_by']

