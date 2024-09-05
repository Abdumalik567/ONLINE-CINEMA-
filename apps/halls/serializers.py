from rest_framework import serializers

from apps.halls.models import Hall

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class HallCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = '__all__'


class HallRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = '__all__'
