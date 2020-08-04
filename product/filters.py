import django_filters
from .models import Brand


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Brand
        fields = {
            'title': ['icontains'],
        }