from django.urls import path
from .views import *

urlpatterns = [
    path('', projects, name='projects'),
    path('create-project/', createProject, name='create-project'),
    path('update-project/<uuid:pk>/', updateProject, name='update-project'),
    path('delete-project/<uuid:pk>/', deleteProject, name='delete-project'),
    path('<uuid:pk>/', project, name='project'),
]
