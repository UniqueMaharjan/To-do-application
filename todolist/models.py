from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True,max_length= 200)
    
    def __str__(self):
        return self.title