from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),  # Accessible at /todo/
    path('new/', TaskCreateView.as_view(), name='task-create'),  # Accessible at /todo/new/
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),  # Accessible at /todo/<pk>/edit/
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),  # Accessible at /todo/<pk>/delete/
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # Accessible at /todo/<pk>/
]
