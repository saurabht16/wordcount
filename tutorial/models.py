from django.db import models

# Create your models here.
# tutorial/models.py
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')


class Customer(models.Model):
    customer_first_name = models.CharField(null=False, blank=False, max_length=50)
    customer_last_name = models.CharField(null=False, blank=False, max_length=50)
    customer_email = models.CharField(null=False, blank=False, max_length=80)
    account_number = models.CharField(null=False, blank=False, max_length=20)
    address1 = models.CharField(null=False, blank=False, max_length=50)
    address2 = models.CharField(null=False, blank=False, max_length=20)
    city = models.CharField(null=False, blank=False, max_length=50)
    state = models.CharField(null=False, blank=False, max_length=2)
    customer_email = models.CharField(null=False, blank=False, max_length=80)
    primary_phone = models.CharField(null=False, blank=False, max_length=12)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


ordering = ['-id']