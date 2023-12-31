from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def projects(request):
#     number = 8
#     page = 'Page 1'
#     context = {'page': page, 'number': number, 'projectList': projectsList}
#     return render(request, 'projects/projects.html', {
#         'context': context
#     })


# def project(request, pk):
#     projectObj = None

#     for project in projectsList:
#         if (project['id'] == pk):
#             projectObj = project
#     return render(request, 'projects/single-project.html', {
#         'code': pk,
#         'project': projectObj
#     })


def projects(request):
    projects = Project.objects.all()
    context = {
        'projectList': projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    # tags = project.tags.all()
    return render(request, 'projects/single-project.html', {
        'project': project,
        # 'tags': tags
    })


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
