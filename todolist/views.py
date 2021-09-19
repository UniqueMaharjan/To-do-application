from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Taskform
from .models import Task

# Create your views here.


def index(request):
    task = Task.objects.all()
    content = {"task": task}
    return render(request, "todolist/index.html", content)


def Aboutus(request):
    return render(request, "todolist/aboutus.html")

def createForm(request):
    taskForm = Taskform()
    if request.method == "POST":
        taskForm = Taskform(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect("index")
    content = {"task": taskForm}
    return render(request, "todolist/task.html", content)

def editForm(request,pk):
    tasks = Task.objects.get(uu_id = pk)
    task_form = Taskform(instance = tasks)
    if request.method == "POST":
        task_form = Taskform(request.POST,instance = tasks)
        if task_form.is_valid:
            task_form.save()
            return redirect('index')
    
    return render(request, "todolist/task.html",{'task':task_form})

def deleteForm(request,pk):
    task = Task.objects.get(uu_id = pk)

    if request.method == "POST":
        task.delete()
        return redirect('index')
    return render(request,'todolist/delete.html',{'object':task})