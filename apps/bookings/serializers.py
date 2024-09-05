from rest_framework import serializers

from apps.bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'


class BookingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'