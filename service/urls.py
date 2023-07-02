from django.urls import path
from service import views

urlpatterns = [
    path('list_of_tasks/', views.ServiceTaskListView.as_view(), name='list-of-tasks'),
    path('create_task/', views.ServiceTaskCreateView.as_view(), name='create-task'),
    path('task_details/<int:pk>/', views.ServiceTaskDetailsView.as_view(), name='task-details'),
    path('task_update/<int:pk>/', views.ServiceTaskUpdateView.as_view(), name='task-update'),
    path('task_delete/<int:pk>/', views.ServiceTaskDeleteView.as_view(), name='task-delete'),
]
