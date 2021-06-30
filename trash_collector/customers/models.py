from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    weekly_pickup_day = models.CharField(max_length=10, null=True)
    onetime_pickup = models.CharField(max_length=10, null=True)
    start_suspension = models.CharField(max_length=10, null=True)
    end_suspension = models.CharField(max_length=10, null=True)
    balance = models.IntegerField(max_length=10, default=0)
    zip_code = models.CharField(max_length=5, null=True)
    address = models.CharField(max_length=50, null=True)

    # suspension = True
    # weekly_pickup_confirmed = True

