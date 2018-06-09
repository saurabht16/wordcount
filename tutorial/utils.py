from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from .models import Customer

class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):

        #qs = super(PagedFilteredTableView, self).get_queryset()
        self.id = self.kwargs['id']
        qs = Customer.objects.filter(pk=self.id)
        print(qs)
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        print('hello')
        print(self.filter)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context