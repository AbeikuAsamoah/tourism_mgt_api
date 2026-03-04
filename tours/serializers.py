from rest_framework import serializers
from .models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'description', 'destination', 'price', 
                  'duration', 'available_slots', 'created_at', 'updated_at', 'organizer']
        read_only_fields = ['created_at', 'updated_at', 'organizer']
