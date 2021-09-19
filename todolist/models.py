from django.db import models
import uuid

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=200)
    uu_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return self.title
