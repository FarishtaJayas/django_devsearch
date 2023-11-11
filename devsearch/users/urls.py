from django.urls import path
from .views import *

urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<uuid:pk>/', userProfile, name='user-profile')
]
