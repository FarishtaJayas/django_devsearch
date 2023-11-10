from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'dev website',
        'description': 'I am doing an awesome project',
    },
    {
        'id': '2',
        'title': 'mobile app development',
        'description': 'Creating a cutting-edge mobile application.',
    },
    {
        'id': '3',
        'title': 'data science project',
        'description': 'Analyzing large datasets to extract valuable insights.',
    },
    {
        'id': '4',
        'title': 'e-commerce platform',
        'description': 'Building an online marketplace for various products.',
    },
    # Add more entries as needed
]


def projects(request):
    number = 8
    page = 'Page 1'
    context = {'page': page, 'number': number, 'projectList': projectsList}
    return render(request, 'projects/projects.html', {
        'context': context
    })


def project(request, pk):
    projectObj = None

    for project in projectsList:
        if (project['id'] == pk):
            projectObj = project
    return render(request, 'projects/single-project.html', {
        'code': pk,
        'project': projectObj
    })
