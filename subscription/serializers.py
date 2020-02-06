from rest_framework import serializers
from .models import Booking

# subscription serializers here


class subscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'subscriber',
            'subscribedTo',
            'quantity',
            'startDate',
            'EndDate',
            'weeks',
            'price',
        )