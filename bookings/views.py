from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

# List bookings (user sees their own)
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

# Create a booking
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)

        # Reduce available slots
        tour = booking.tour
        tour.available_slots -= 1
        tour.save()

# Cancel a booking
class BookingCancelView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        booking = serializer.save(status='cancelled')

        # Restore slot
        tour = booking.tour
        tour.available_slots += 1
        tour.save()
