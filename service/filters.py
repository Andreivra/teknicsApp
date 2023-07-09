import django_filters
from django import forms
from django_filters import DateFilter
from service.models import Company


class TaskFilters(django_filters.FilterSet):
    get_tasks = [(company.agent_name, company.agent_name) for company in Company.objects.filter(active=True)]

    company_name = django_filters.CharFilter(lookup_expr='icontains', label='Company name')
    contact_name = django_filters.CharFilter(lookup_expr='icontains', label='Contact name')
    email = django_filters.CharFilter(lookup_expr='exact', label='Email')
    agent_name = django_filters.ChoiceFilter(choices=list(set(get_tasks)))
    start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Company
        fields = ['company_name', 'contact_name', 'email', 'start_date_gte', 'start_date_lte', 'agent_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['company_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter company name'})
        self.filters['contact_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter contact name'})
        self.filters['email'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter email'})
        self.filters['agent_name'].field.widget.attrs.update({'class': 'form-select'})
