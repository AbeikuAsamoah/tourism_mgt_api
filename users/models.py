from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """
    Custom user model for a tourism platform.
    Supports tourists and admin/staff users.
    """

    class Role(models.TextChoices):
        TOURIST = 'tourist', 'Tourist'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.TOURIST
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def is_tourist(self):
        return self.role == self.Role.TOURIST

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def save(self, *args, **kwargs):
        """
        Automatically sync Django permissions with role.
        """
        if self.role == self.Role.ADMIN:
            self.is_staff = True
        else:
            self.is_staff = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
