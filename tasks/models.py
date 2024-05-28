from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS = [
        ('Not-started', 'Not-started'),
        ('To-do', 'To-do'),
        ('In-progress', 'In-progress'),
        ('Completed', 'Completed'),
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    overdue = models.BooleanField(default=False)
    assigned_users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True, 
        related_name='assigned_to')
    priority = models.CharField(max_length=255, choices=PRIORITY_CHOICES, default='Low')
    state = models.CharField(max_length=255, choices=STATUS, default='Not-started')
    attachment = models.ImageField(
        upload_to = 'images/', default='../default_post_t6ubcp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} {self.title}"