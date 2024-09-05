from rest_framework import viewsets

from apps.ratings.models import Rating
from apps.ratings.serializers import (
    RatingSerializer,
    RatingCreateUpdateSerializer,
    RatingRetrieveSerializer
)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return RatingRetrieveSerializer
        return RatingCreateUpdateSerializer
