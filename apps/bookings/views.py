from rest_framework import viewsets

from apps.bookings.models import Booking
from apps.bookings.serializers import (
    BookingSerializer,
    BookingCreateUpdateSerializer,
    BookingRetrieveSerializer
)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return BookingRetrieveSerializer
        return BookingCreateUpdateSerializer

