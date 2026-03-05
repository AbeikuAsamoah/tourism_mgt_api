from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'tour', 'status', 'created_at']
        read_only_fields = ['user', 'status', 'created_at']

    def validate(self, attrs):
        tour = attrs['tour']
        user = self.context['request'].user

        # Prevent duplicate booking
        if Booking.objects.filter(user=user, tour=tour).exists():
            raise serializers.ValidationError(
                "You have already booked this tour."
            )

        # Prevent booking if no slots left
        if tour.available_slots <= 0:
            raise serializers.ValidationError(
                "No available slots for this tour."
            )

        return attrs
