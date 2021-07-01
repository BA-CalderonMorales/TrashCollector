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
    if not Customer.objects.filter(user_id=user.id).exists():
        #  If user isn't in current Customer database, then create a customer with user information.
        return redirect('create/')
    else:
        # Go into the home portal with user information found in Customer database.

        specific_customer = Customer.objects.get(user_id=user.id)
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
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def edit(request):
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    context = {
        'specific_customer': specific_customer
    }
    if request.method == 'POST':
        specific_customer.name = request.POST.get('name')
        specific_customer.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        specific_customer.address = request.POST.get('address')
        specific_customer.zip_code = request.POST.get('zip_code')
        specific_customer.one_time_pickup = request.POST.get('one_time_pickup')
        specific_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/edit.html', context)
