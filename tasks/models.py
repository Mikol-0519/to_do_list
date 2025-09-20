from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    due_date = models.DateField(blank=True, null=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"
