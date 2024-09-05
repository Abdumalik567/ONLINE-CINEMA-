from rest_framework import viewsets

from apps.reviews.models import Review
from apps.reviews.serializers import (
    ReviewSerializer,
    ReviewCreateUpdateSerializer,
    ReviewRetrieveSerializer
)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return ReviewRetrieveSerializer
        return ReviewCreateUpdateSerializer