from django.urls import path

from .views import task_list, task_create, task_detail, task_update, task_delete

urlpatterns = [
    path('todos/', task_list, name='task-list'),
    path('todos/create/', task_create, name='task-create'),
    path('todos/<int:pk>/', task_detail, name='task-detail'),
    path('todos/<int:pk>/update/', task_update, name='task-update'),
    path('todos/<int:pk>/delete/', task_delete, name='task-delete'),

]