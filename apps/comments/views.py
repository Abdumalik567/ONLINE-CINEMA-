from rest_framework import viewsets

from apps.comments.models import Comment
from apps.comments.serializers import (
    CommentSerializer,
    CommentCreateUpdateSerializer,
    CommentRetrieveSerializer
)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update']:
            return CommentRetrieveSerializer
        return CommentCreateUpdateSerializer
