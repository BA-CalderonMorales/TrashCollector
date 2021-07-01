from django.db import models

# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.PROTECT)
    weekly_pickup_day = models.CharField(max_length=10, blank=True, null=True)
    onetime_pickup = models.CharField(max_length=10, blank=True, null=True)
    start_suspension = models.CharField(max_length=10, blank=True, null=True)
    end_suspension = models.CharField(max_length=10, blank=True, null=True)
    balance = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=00000, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    # is_new_customer = True
    has_suspension = models.BooleanField(default=False)

