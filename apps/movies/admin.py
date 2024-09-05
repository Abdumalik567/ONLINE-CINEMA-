from django.contrib import admin

from apps.movies.models import Movie,Like,Payment,Subtitle,Genre,Award,Wishlist,Actor,MovieSession,Order,Ticket
from apps.movies.filters import MovieFilter





admin.site.register(Movie)
admin.site.register(Like)
admin.site.register(Payment)
admin.site.register(Subtitle)
admin.site.register(Genre)
admin.site.register(Award)
admin.site.register(Wishlist)
admin.site.register(Actor)
admin.site.register(MovieSession)
admin.site.register(Order)
admin.site.register(Ticket)



