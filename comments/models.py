from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

class Comments(models.Model):
    """
    A class model for the comments
    Related to User and Task
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content