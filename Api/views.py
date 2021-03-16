from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


# def apioverview(request):
#     """result ll be in json format"""
#     return JsonResponse("API BASE POINT", safe=False)

"""
Response object, which is a type of TemplateResponse
@api_view decorator for working with function based views
These wrappers provide a few bits of functionality
such as making sure you receive Request instances in your view,
and adding context to Response objects 
"""


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

# Django’s serialization framework provides a mechanism for “translating” Django models into other formats.
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Getting Specific Object in a Task Model
@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)
