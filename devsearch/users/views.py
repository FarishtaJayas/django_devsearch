from django.shortcuts import render
from .models import *
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    user_data = Profile.objects.get(id=pk)

    top_skills = user_data.skill_set.exclude(description__exact="")
    other_skills = user_data.skill_set.filter(description="")

    context = {'profile': user_data, 'top_skills': top_skills,
               'other_skills': other_skills, }
    return render(request, 'users/user-profile.html', context)
