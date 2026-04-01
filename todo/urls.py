from django.urls import path

from .views import task_list, task_create

urlpatterns = [
    path('todos/', task_list, name='task-list'),
    path('todos/create/', task_create, name='task-create'),
]