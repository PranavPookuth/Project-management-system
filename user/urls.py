from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserlistView.as_view(), name='user-list'),
    path('activity-logs/', ActivityLogListCreateView.as_view(), name='activity-log'),
]