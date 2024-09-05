from rest_framework import viewsets

from apps.tags.models import Tag
from apps.tags.serializers import (
    TagSerializer,
    TagCreateUpdateSerializer,
    TagRetrieveSerializer
)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return TagRetrieveSerializer
        return TagCreateUpdateSerializer