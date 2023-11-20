from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('', profiles, name='profiles'),
    path('account/', userAccount, name='account'),
    path('profile/<uuid:pk>/', userProfile, name='user-profile'),
    path('edit-account/', editAccount, name='edit-account'),

    path('create-skill', createSkill, name='create-skill'),
    path('update-skill/<uuid:pk>/', updateSkill, name='update-skill'),
]
