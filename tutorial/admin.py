from django.contrib import admin
from tutorial.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('customer_first_name',)

admin.site.register(Customer, CustomerAdmin)
