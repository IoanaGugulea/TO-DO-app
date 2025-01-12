from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('task_list')  # Redirect to the task list
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Home page - List all tasks
@login_required
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks for the logged-in user
    return render(request, 'task_list.html', {'tasks': tasks})

# Add a new task

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associate the task with the logged-in user
            task.save()
            return redirect('task_list')  # Redirect to the task list after saving the task
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Ensure the task belongs to the logged-in user
    if request.method == 'POST':
        # Toggle the completed status
        task.completed = not task.completed
        task.save()
        return redirect('task_list')
    return render(request, 'add_task.html', {'form': TaskForm(instance=task)})

# Delete a task
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Ensure the task belongs to the logged-in user
    task.delete()
    return redirect('task_list')


