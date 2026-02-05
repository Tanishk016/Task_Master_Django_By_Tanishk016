# todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords

class Task(models.Model):
    title = models.CharField(max_length=200)       # The task name
    completed = models.BooleanField(default=False) # Is it done?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    history = HistoricalRecords()

    def __str__(self):
        return self.title