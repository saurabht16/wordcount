# Create your views here.

from django.shortcuts import render
from .models import Person
from django_tables2 import RequestConfig
from tutorial.models import Person
from tutorial.tables import PersonTable

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

import django_filters

from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django_tables2 import RequestConfig
from .tables import CustomerTable
from .filters import CustomerListFilter
from .utils import PagedFilteredTableView
from .models import Customer
from .forms import CustomerListFormHelper


class CustomerListView(PagedFilteredTableView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customer'
    ordering = ['-id']
    group_required = u'company-user'
    table_class = CustomerTable
    filter_class = CustomerListFilter
    formhelper_class = CustomerListFormHelper

    def get_queryset(self):
        qs = super(CustomerListView, self).get_queryset()
        #self.id = self.kwargs['id']
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['nav_customer'] = True
        search_query = self.get_queryset()
        table = CustomerTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['name']


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    #template_name = 'tutorial/people.html'

    filterset_class = PersonFilter


def people(request):
    filter = PersonFilter(request.GET, queryset=Person.objects.all())
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    print(table)
    return render(request, 'tutorial/people.html', {'table': table, 'filter': filter})

