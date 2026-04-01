from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.serializers import TaskSerializer
from .models import Task
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({
        "success": True,
        "message": "Tasks retrieved successfully",
        "data": serializer.data
    })

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Task created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "success": False,
        "message": "Failed to create task",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
