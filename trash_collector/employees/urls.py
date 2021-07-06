from django.urls import path
from . import views


# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('daily/', views.find_customers_by_day, name='daily'),
    path('daily/<str:option>/', views.find_customers_by_day, name='daily'),
    path(r'confirmed_pickup/^objects/(?P<oid>[0-9]+)/$', views.confirmed_pickups, name='confirmed_pickup')
]