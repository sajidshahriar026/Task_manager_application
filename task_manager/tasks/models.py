from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Task(models.Model):
    PRIORITY = {
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    }
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    priority = models.IntegerField(blank=False, choices=PRIORITY)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Images(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_image = models.ImageField(upload_to="task_images")

