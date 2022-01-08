from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=150,null=True)
    email = models.EmailField(unique=True,null=True)
    photo = models.ImageField(default = 'images/avatar.svg',upload_to = "images/",null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Task(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
