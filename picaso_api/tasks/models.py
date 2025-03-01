from django.db import models

class Task(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In-progress'
    DONE = 'Done'
    
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In-progress'),
        (DONE, 'Done'),
    ]
    
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    
    def __str__(self):
        return self.title
