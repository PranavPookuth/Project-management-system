from django.db import models
from user.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
