from rest_framework import viewsets,mixins
from rest_framework.viewsets import GenericViewSet

from apps.halls.models import Hall
from apps.halls.serializers import (
    HallSerializer,
    HallCreateUpdateSerializer,
    HallRetrieveSerializer
)
from apps.movies.permissions import IsAdminOrOwnerPermission

class HallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = (IsAdminOrOwnerPermission,)
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return HallRetrieveSerializer
        return HallCreateUpdateSerializer