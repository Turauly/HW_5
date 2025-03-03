from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# 🔹 Логин функциясы
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
        else:
            return render(request, 'registration/login.html', {'error': 'Қате логин немесе құпия сөз'})
    return render(request, 'registration/login.html')

@login_required  # 🔥 Тек авторизациядан өткен қолданушылар шыға алады
def logout_view(request):
    logout(request)  # 🔥 Пайдаланушыны шығару
    return redirect('login')  # 🔄 Логин бетіне қайта бағыттау

# 🔹 Тек тіркелген қолданушыларға ғана қолжетімді беттер
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo_list')
