from django.db import models

# Create your models here.
class ToDoList(models.Model):
    todolist=models.CharField(max_length=200)
    date=models.DateTimeField(max_length=50)

    def __str__(self):
        return self.todolist