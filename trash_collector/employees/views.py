from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.apps import apps

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
        specific_employee = Employees.objects.get(user_id=user.id)
        all_customers = Customer.objects.all()
        context = {
            'user': user,
            'all_customers': all_customers,
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