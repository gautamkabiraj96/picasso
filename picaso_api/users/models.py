from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure an email address is provided
        if not email:
            raise ValueError('User must have an email address')
        # Normalize the email address to standard format
        email = self.normalize_email(email)
        # Create and save the user instance
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set flags for admin-level user
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Create and return a superuser using the same logic as create_user
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        default="default_user"  # Generates a unique default username
    )
    # Add custom fields here
    profile_picture = models.URLField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    # Make email the USERNAME_FIELD
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    
    # List of required fields that need to be provided upon user creation
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
