from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .serializers import ToDoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_todo_list(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def todo_list_create(request):
    filter_param = request.GET.get('filter')
    todos = ToDo.objects.filter(user=request.user)

    if filter_param == 'done':
        todos = todos.filter(is_completed=True)
    elif filter_param == 'undone':
        todos = todos.filter(is_completed=False)

    todos = todos.order_by('-created_at')

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list_create')
    else:
        form = ToDoForm()

    return render(request, 'todo/todo_list.html', {'form': form, 'todos': todos})



@login_required
def edit_task(request, pk):
    task = get_object_or_404(ToDo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list_create')
    else:
        form = ToDoForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(ToDo, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list_create')
    return render(request, 'todo/confirm_delete.html', {'task': task})