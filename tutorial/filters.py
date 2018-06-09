# filters.py
import django_filters
from .models import Customer

class AccountFilter(django_filters.ChoiceFilter):

    @property
    def field(self):
        self.extra['choices'] = [(a.account_number, a.account_number) for a in self.parent.queryset]
        return super(AccountFilter, self).field


class CustomerListFilter(django_filters.FilterSet):
    account_number = AccountFilter(
        field_name='account_number',

    )

    class Meta:
        model = Customer
        fields = ['account_number', 'customer_first_name',]


    order_by = ['pk']