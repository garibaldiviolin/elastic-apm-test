from django_filters import FilterSet

from .models import Product


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = ('slug', 'description',)
