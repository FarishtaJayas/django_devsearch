from django.urls import path
from .views import *

urlpatterns = [
    path('', projects, name='projects'),
    path('create-project/', createProject, name='create-project'),
    path('<str:pk>/', project, name='project'),
]
