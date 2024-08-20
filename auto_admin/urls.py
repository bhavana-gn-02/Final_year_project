from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('adminpage/',adminpage),

   
    path('change_pass/',change_pass),
    path('custvehicle_view/',custvehicle_view),
    path('driverhome/', driverhome),
    path('customer_details/',customer_details),
    path('customer_add/',customer_add),
    path('customer_view/',customer_view),
    path('customer_delete/<int:customer_id>',customer_delete),
    path('customer_update/<int:customer_id>',customer_update),
    path('customer_edit/<int:customer_id>',customer_edit),
    path('customer_profile/',customer_profile),

    path('driverchange_pass/',driverchange_pass),
    path('driver/',driver),
    path('driver_add/',driver_add),
    path('drivers_view/',drivers_view),
    path('driver_delete/<int:driver_id>',driver_delete),
    path('driver_update/<int:driver_id>',driver_update),
    path('driver_edit/<int:driver_id>',driver_edit),
    path('driver_profile/',driver_profile),
    path('driverpage/',driverpage),
    path('driveridebook/',driveridebook),
    path('driverpay/',driverpay),

    path('ridebook/<int:dr_id>',ridebook),
    path('ridebook_add/',ridebook_add),
    path('ridebook_view/',ridebook_view),
    path('ridebook_delete/<int:ridebook_id>',ridebook_delete),
    path('ridebook_update/<int:ridebook_id>',ridebook_update),
    path('ridebook_edit/<int:ridebook_id>',ridebook_edit),

    path('routes1/',routes1),
    path('routes_add/',routes_add),
    path('routes_view/',routes_view),
    path('routes_delete/<int:rout_id>',routes_delete),
    path('routes_update/<int:rout_id>',routes_update),
    path('routes_edit/<int:rout_id>',routes_edit),
    
    path('payment1/<int:ridebook_id>',payment1),
    path('payment_add/',payment_add),
    path('payment_view/',payment_view),
   

    path('vehical/',vehical),
    path('vehical_location_add/',vehical_location_add),
    path('vehical_location_view/',vehical_location_view),
    path('vehical_location_delete/<int:v_id>',vehical_location_delete),
    path('vehical_location_update/<int:v_id>',vehical_location_update),
    path('vehical_location_edit/<int:v_id>',vehical_location_edit)

    

   

]