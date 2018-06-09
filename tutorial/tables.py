# tutorial/tables.py.py
import django_tables2 as tables
from .models import Person
from django_tables2.utils import A
from .models import Customer

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'





class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        fields = ('account_number', 'customer_first_name',
                  'customer_last_name', 'primary_phone', 'city',
                  'state', 'customer_email')
        attrs = {"class": "table-striped table-bordered"}
        template_name = 'django_tables2/bootstrap.html'


empty_text = "There are no customers matching the search criteria..."