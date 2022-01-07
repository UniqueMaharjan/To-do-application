from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task,User
from .forms import Taskform,UserCreation,UserForm


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request,"User doesn't exist!!!")
        
        user = authenticate(request,email = email,password = password)
        if user != None:
            login(request,user)
            return redirect('home')
    context = {'page':page,}
    return render(request,'todolist/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreation()
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Registration Fail!!')
    context = {'form':form}
    return render(request,'todolist/login.html',context)


@login_required(login_url='login')
def home(request):
    form = Taskform()
    task = Task.objects.filter(host = request.user)
    completed_task = Task.objects.filter(host = request.user,completed = True).count()
    uncompleted_task = task.count()
    
    context = {'task':task,'form':form,'uncompleted':uncompleted_task,'completed':completed_task,}
    return render(request,'todolist/home.html',context)

@login_required(login_url='login')
def createTask(request):
    form = Taskform()
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(
            host = request.user,
            task = task
        )
        
        return redirect('home')

    
    return render(request,'todolist/create-task.html',{'form':form})

@login_required(login_url='login')
def editTask(request,pk):
    page = "edit"
    task = Task.objects.get(id = pk)
    form = Taskform(instance=task)
    if request.method == "POST":
        form = Taskform(request.POST,instance = task)
        form.save()
        return redirect('home')
    return render(request,'todolist/create-task.html',{'form':form,'page':page})

@login_required(login_url='login')
def deleteTask(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('home')

def editUser(request):
    user = User.objects.get(email = request.user.email)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'todolist/editprofile.html',{'form':form})

    