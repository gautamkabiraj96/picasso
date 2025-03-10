from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

class User(AbstractBaseUser):
    # User's email address, used as username
    email = models.EmailField(unique=True)
    # User's first and last names
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Boolean fields to track user's active status and staff status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Timestamps for when the user object was created and last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # UserManager instance to handle user creation and authentication
    objects = UserManager()

    # Custom User model specifies the email as the unique identifier
    USERNAME_FIELD = 'email'
    # List of required fields that need to be provided upon user creation
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        # String representation of the User model, returning the user's email
        return self.email

class AccessTokenBlacklist(models.Model):
    token = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
