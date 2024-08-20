from django.contrib import admin
from .models import *
# Register your models here.
class customeradmin(admin.ModelAdmin):
    list_display=('id','cname','email','contact','passwrd')
    
admin.site.register(customer,customeradmin)

class driverzadmin(admin.ModelAdmin):
    list_display=('id','dname','email','passw','contact','auto_number','auto_type','auto_date','license_no','auto_photo','driver_photo')

admin.site.register(driverz,driverzadmin)

class routesadmin(admin.ModelAdmin):
    list_display=('id','froute','troute')

admin.site.register(routes,routesadmin)

class ridebookadmin(admin.ModelAdmin):
    list_display=('id','cid','did','froute','troute','total_km','perkm_cost','total_amount','book_date','book_time','book_status')
    
admin.site.register(ride_book,ridebookadmin)

class paymentsadmin(admin.ModelAdmin):
    list_display=('id','rbook_id','t_type','t_amount','t_date')

admin.site.register(payment,paymentsadmin)

class locationadmin(admin.ModelAdmin):
    list_display=('id','did','zipcode','city','country','adress','map_location','driver_photo')

admin.site.register(vehical_location,locationadmin)

