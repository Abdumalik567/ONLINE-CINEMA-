from django.db import models
from django.contrib.auth import get_user_model

from apps.movies.models import Movie

User = get_user_model()

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments', 
        null=True,
        blank=True,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='movies',
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.text
