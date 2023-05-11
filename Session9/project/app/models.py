from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
    
    def get_d_day(self):
        delta = self.deadline - datetime.now().date()
        return delta.days
