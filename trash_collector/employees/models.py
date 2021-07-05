from django.db import models


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.PROTECT)
    zip_code = models.IntegerField(default=00000, null=True)
    customer_list = []

# TODO: Create an Employee model with properties required by the user stories
