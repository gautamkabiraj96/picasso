from django.db import models
from users.models import User

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'New'
        IN_PROGRESS = 'In-progress', 'In-progress'
        DONE = 'Done', 'Done'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    def __str__(self):
        return f"{self.title} ({self.status})"
