from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PRIORITY = {
        (3, 'Low'),
        (2, 'Medium'),
        (1, 'High'),
    }
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    priority = models.IntegerField(blank=False, choices=PRIORITY)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def created_by(self):
        return self.user.username

    def completed(self):
        return self.is_complete



class Image(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_image = models.ImageField(upload_to="task_images")

    def __str__(self):
        return str(self.task.title)

