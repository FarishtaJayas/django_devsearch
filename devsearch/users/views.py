from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return render(request, 'users/login_register.html', {'page': page})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created")

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(
                request, "An error has occurred during registration")
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


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


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'users/account.html', context)
