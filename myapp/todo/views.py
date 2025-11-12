from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

# List all tasks
class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

# Create a new task 
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

# Update a task
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

# Delete a task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

# View a single task
class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'