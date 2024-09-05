from rest_framework import serializers

from apps.ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'


class RatingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
