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


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({
            "success": False,
            "message": "Task not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task)
    return Response({
        "success": True,
        "message": "Task retrieved successfully",
        "data": serializer.data
    })

@api_view(['PUT'])
def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({
            "success": False,
            "message": "Task not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Task updated successfully",
            "data": serializer.data
        })
    return Response({
        "success": False,
        "message": "Failed to update task",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({
            "success": False,
            "message": "Task not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response({
        "success": True,
        "message": "Task deleted successfully"
    }, status=status.HTTP_204_NO_CONTENT)


