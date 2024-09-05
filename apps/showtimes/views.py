from rest_framework import viewsets

from apps.showtimes.models import Showtime
from apps.showtimes.serializers import (
    ShowtimeSerializer,
    ShowtimeCreateUpdateSerializer,
    ShowtimeRetrieveSerializer
)

class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return ShowtimeRetrieveSerializer
        return ShowtimeCreateUpdateSerializer

