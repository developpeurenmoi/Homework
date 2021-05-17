from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField()
    author = models.ForeignKey(User, on_delete = models.CASCADE,
    related_name='todos', null=True, default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, default=None)