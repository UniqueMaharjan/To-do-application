from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Taskform
from .models import Task
# Create your views here.

def index(request):
    task = Task.objects.all()
    content = {
        'task':task
    }
    return render(request,'todolist/index.html',content)

def Aboutus(request):
    return render(request,'todolist/aboutus.html')

# def Task_form(request):
#     task = Task()
#     content = {
#         'task':task
#     }
#     return render(request,'todolist/task.html',content)

def createForm(request):
    taskForm = Taskform()
    if request.method == "POST":
        taskForm = Taskform(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('index')
    content = {
        'task': taskForm
    }
    return render(request,'todolist/task.html',content)