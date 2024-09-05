from django.db import models
from django.contrib.auth import get_user_model

from apps.showtimes.models import Showtime

User = get_user_model()

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.user.username} - {self.showtime.movie.title} ({self.showtime.start_time})"