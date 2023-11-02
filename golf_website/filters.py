from decimal import Decimal
from django.db.models import Q
import django_filters
from golf_website.models import Swing

class SwingFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Swing
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Swing.objects.filter(Q(distance=value) | Q(swing_speed=value))

        return Swing.objects.filter(Q(swing_time__icontains=value))
