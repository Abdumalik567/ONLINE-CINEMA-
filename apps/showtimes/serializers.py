
from rest_framework import serializers

from apps.showtimes.models import Showtime

class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = '__all__'


class ShowtimeCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showtime
        fields = '__all__'


class ShowtimeRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showtime
        fields = '__all__'
