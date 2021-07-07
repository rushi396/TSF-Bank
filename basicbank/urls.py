from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('transfer_money/',views.cust, name= 'transfermoney'),
    path('transfer_details/',views.transfer, name= 'transferdetails'),
    path('customers/',views.cdetails, name= 'customers'),
]