import django_filters

from apps.movies.models import Movie,Like

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    release_date = django_filters.DateFilter(lookup_expr='exact')

    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'tags', 'hall']


class LikeFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name='user', lookup_expr='exact')
    movie = django_filters.NumberFilter(field_name='movie', lookup_expr='exact')

    class Meta:
        model = Like
        fields = ['user', 'movie']