from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('', profiles, name='profiles'),
    path('profile/<uuid:pk>/', userProfile, name='user-profile')
]
