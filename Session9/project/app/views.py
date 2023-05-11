from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    for todo in todos:
        todo.d_day = todo.get_d_day()

    todos = sorted(todos, key=lambda x: x.d_day)

    return render(request, 'home.html', {'todos': todos})


def new(request):
    if request.method == 'POST':
        new_post = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', new_post.pk)
    
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Todo.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Todo.objects.get(pk=post_pk)

    if request.method == 'POST':
        Todo.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail',post_pk)
    
    return render(request,	'update.html',	{'post':post})


def delete(request, post_pk):
    post = Todo.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')
