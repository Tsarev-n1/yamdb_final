from django_filters import FilterSet, CharFilter

from reviews.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(lookup_expr='icontains', field_name='genre__slug')
    category = CharFilter(lookup_expr='icontains', field_name='category__slug')
    name = CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')
