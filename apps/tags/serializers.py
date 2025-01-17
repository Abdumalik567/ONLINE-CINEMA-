from rest_framework import serializers

from apps.tags.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TagRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'