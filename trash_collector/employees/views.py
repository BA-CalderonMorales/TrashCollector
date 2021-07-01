from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.apps import apps
import time
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")
print(today)
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
from django.urls import reverse
from .models import Employees


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    if not Employees.objects.filter(user_id=user.id).exists():
        #  If user isn't in current Employee database, then create an employee with user information.
        return redirect('create/')
    else:
        # Go into the home portal with user information found in Employee database.
        all_customers = Customer.objects.all()
        specific_employee = Employees.objects.get(user_id=user.id)
        same_zip_and_not_suspended = all_customers.filter(zip_code=specific_employee.zip_code)
        #one_time_pickup = same_zip_customers.filter(onetime_pickup=)
        context = {
            'user': user,
            'todays_customers': todays_customers,
            'specific_employee': specific_employee
        }
        print(user)
        return render(request, 'employees/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(
            user_id=request.user.id,
            name=name,
            zip_code=zip_code,
        )
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')