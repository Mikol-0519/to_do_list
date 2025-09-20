from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .models import TaskForm

def task_list(request):
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_type == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter': filter_type})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('task_list')

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
