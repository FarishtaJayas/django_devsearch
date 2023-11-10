from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def projects(request):
    number = 11
    page = 'Page 1'
    context = {'page': page, 'number': number}
    return render(request, 'projects/projects.html', {
        'context': context
    })


def project(request, pk):
    return render(request, 'projects/single-project.html', {
        'code': pk
    })
