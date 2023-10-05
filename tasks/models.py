from django.contrib.auth.models import AbstractUser
from django.db import models

class Task(models.Model):
     title=models.CharField(max_length=200)
     description=models.TextField()
     completed=models.BooleanField(default=False)
     class Meta:
          db_table="Task"

# Create your models here.
