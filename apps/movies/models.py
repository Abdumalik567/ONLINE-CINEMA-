import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def movie_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/movies/", filename)



class Movie(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField(
    )
    release_date = models.DateField(
    )
    duration = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    video = models.FileField(
        upload_to='movies/videos/',
        null=True, blank=True
    )
    picture = models.ImageField(
        upload_to='movies/pictures/',
        null=True, blank=True
    )
    trailer = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movies',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        'tags.Tag',  
        related_name='movies',
        blank=True,
    )
    hall = models.ForeignKey(
        'halls.Hall', 
        on_delete=models.SET_NULL,
        related_name='movies',
        null=True,
        blank=True,
    )
    showtimes = models.ManyToManyField(
        'showtimes.Showtime',  
        related_name='movies',
        blank=True,
    )
    reviews = models.ManyToManyField(
        'reviews.Review',  
        related_name='movies',
        blank=True,
    )
    bookings = models.ManyToManyField(
        'bookings.Booking',  
        related_name='movies',
        blank=True,
    )
    ratings = models.ManyToManyField(
        'ratings.Rating', 
        related_name='movies',
        blank=True,
    )
    comments = models.ManyToManyField(
        'comments.Comment',  
        related_name='movies',
        blank=True,
    )
    slug = models.SlugField(
     unique=True,
     blank=True,
     null=True,
    )
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
         return self.title
    
    def average_rating(self):
        return self.ratings.aggregate(Avg('value'))['value__avg']
    
    def total_likes(self):
        return self.likes.count()


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey('halls.Hall', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return self.movie.title + " " + str(self.show_time)

class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user} likes {self.movie}"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='payments')


class Subtitle(models.Model):
    language = models.CharField(max_length=50)
    file = models.FileField(upload_to='movies/subtitles/')
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        related_name='subtitles'
    )

    def __str__(self):
        return f"{self.language} subtitles for {self.movie.title}"
    




class Award(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.movie.title}"



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} wishes to watch {self.movie.title}"

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]

class Ticket(models.Model):
    movie_session = models.ForeignKey(
        MovieSession, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    @staticmethod
    def validate_ticket(row, seat, cinema_hall, error_to_raise):
        for ticket_attr_value, ticket_attr_name, cinema_hall_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(cinema_hall, cinema_hall_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                        f"number must be in available range: "
                        f"(1, {cinema_hall_attr_name}): "
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.movie_session.cinema_hall,
            ValidationError,
        )

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return (
            f"{str(self.movie_session)} (row: {self.row}, seat: {self.seat})"
        )

    class Meta:
        unique_together = ("movie_session", "row", "seat")
        ordering = ["row", "seat"]