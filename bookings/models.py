from django.db import models
from users.models import CustomUser
from tours.models import Tour

# Create your models here.
class Booking(models.Model):
    """
    Represents a booking made by a tourist for a tour.
    """

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.tour.title} ({self.status})"
