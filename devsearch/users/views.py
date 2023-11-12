from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import *

# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or Password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


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
