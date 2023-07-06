from django.urls import path
from agent import views

urlpatterns = [
    path('create_agent/', views.AgentCreateView.as_view(), name='create-agent'),
    path('list_of_agents/', views.AgentListView.as_view(), name='list-of-agents'),
]
