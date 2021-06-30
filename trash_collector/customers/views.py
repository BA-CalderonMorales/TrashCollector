from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    all_customers = Customer.objects.all()
    context = {
        'user': user,
        'all_customers': all_customers
    }
    print(user)
    return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.POST.get('alter_ego')
        start_break = request.POST.get('primary_ability')
        end_break = request.POST.get('secondary_ability')
        balance = request.POST.get('catchphrase')
        zip_code = request.POST.get('zip_code')
        address = request.POST.get('balance')
        is_new_customer = request.POST.get('is_new_customer')
        new_customer = Customer(
            name=name,
            user=user,
            start_suspension=start_break,
            end_suspension=end_break,
            balance=balance,
            zip_code=zip_code,
            address=address,
            is_new_customer=is_new_customer
        )
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')
