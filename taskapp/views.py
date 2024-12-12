from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task

# Create your views here.

def AddTask(request):
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    tasks = Task.objects.all()
    context = {'tasks':tasks,'TaskForm':form}
    return render(request,'createtask.html',context)

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)

    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'TaskForm':form}
    return render(request,'update.html',context)


def delete_task(request,pk):
    task = Task.objects.get(id=pk)

    if request.method=="POST":
        task.delete()
       
        return redirect('/')
    context={'task':task}
    return render(request,'delete.html',context)

