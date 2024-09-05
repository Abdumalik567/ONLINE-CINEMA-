from django.db import models
from django.contrib.auth import get_user_model

from apps.movies.models import Movie

User = get_user_model()

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])


    def __str__(self):
        return  self.movie.title
    
    