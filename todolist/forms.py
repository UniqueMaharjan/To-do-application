from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Task,User

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']
class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['task','completed']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['photo','name','username','email']