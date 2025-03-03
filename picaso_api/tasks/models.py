from django.db import models

class Task(models.Model):
    # Define status constants
    NEW = 'New'
    IN_PROGRESS = 'In-progress'
    DONE = 'Done'
    
    # Choices for the status field with display-friendly labels
    STATUS_CHOICES = [
        (NEW, 'New'),  # Represents a new, unstarted task
        (IN_PROGRESS, 'In-progress'),  # Represents a task currently being worked on
        (DONE, 'Done'),  # Represents a task that has been completed
    ]
    
    # Field to store the title of the task
    title = models.CharField(max_length=255)
    # Field to store the current status of the task, defaulting to NEW
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    
    def __str__(self):
        # String representation of the model, returning the task title
        return self.title
