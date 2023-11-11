from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
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


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
