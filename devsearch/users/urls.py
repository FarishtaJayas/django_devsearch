from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('', profiles, name='profiles'),
    path('account/', userAccount, name='account'),
    path('profile/<uuid:pk>/', userProfile, name='user-profile')
]
