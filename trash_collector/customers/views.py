from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    if Customer.objects.filter(pk=user.id).exists() == False:
        return redirect('create/')
    else: #home portal
        specific_customer = Customer.objects.get(pk=user.id)
        context = {
            'user': user,
            'specific_customer': specific_customer
        }
        print(user)
        return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        one_time_pickup = request.POST.get('one_time_pickup')
        new_customer = Customer(
            user_id=request.user.id,
            name=name,
            weekly_pickup_day=weekly_pickup_day,
            onetime_pickup=one_time_pickup,
            address=address,
            zip_code=zip_code,
        )
        new_customer.save()
        return render(request, 'customers/index.html')
    else:
        return render(request, 'customers/create.html')
