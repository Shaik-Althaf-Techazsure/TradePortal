import django_filters
from .models import Company

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'company_name': ['icontains'],
            'symbol': ['exact'],
            'scripcode': ['exact'],
        }