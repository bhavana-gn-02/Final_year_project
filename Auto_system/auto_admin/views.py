from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import datetime
from django.db.models import Q
def adminpage(request):
     tc=customer.objects.all().count()
     td=driverz.objects.all().count()
     tr=ride_book.objects.all().count()
     trc=ride_book.objects.filter(book_status = 'completed').count()
     trr=ride_book.objects.filter(book_status = 'Rejected').count()
     
     if 'q' in request.GET:
        q = request.GET['q']
        
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(adress__icontains=q)  )
        
        data = vehical_location.objects.filter(multiple_q)
     else:
        data = vehical_location.objects.all()
        
     context = {
        'data': data,
        'tc':tc,
        'td':td,
        'tr':tr,
        'trc':trc,
        'trr':trr
    }
     #vehl=vehical_location.objects.all()
     return render(request,"adminz/home.html",context)

def driverpage(request):
     tc1=customer.objects.all().count()
     td1=driverz.objects.all().count()
     tr1=ride_book.objects.all().count()
     trc1=ride_book.objects.filter(book_status = 'completed').count()
     trr1=ride_book.objects.filter(book_status = 'Rejected').count()
     
     context1 = {
        'tc1':tc1,
        'td1':td1,
        'tr1':tr1,
        'trc1':trc1,
        'trr1':trr1
    }
     return render(request,"adminz/driver_home.html",context1)

def driveridebook(request):
     userid=request.session['driver_id']
     dridebooks=ride_book.objects.all()
     return render(request,"adminz/driverridebook_view.html",{'dridebooks':dridebooks})

def driverpay(request):
     pay=payment.objects.all()
     return render(request,"adminz/driverpay_view.html",{'pay':pay}) 

def driverhome(request):
     return render(request,"adminz/driver_home.html")

def change_pass(request):
     return render(request,'adminz/change_password.html')
     
def driverchange_pass(request):
     return render(request,'adminz/driverchange_password.html')

def custvehicle_view(request):
     return render(request,'adminz/customer_vehicle_view.html')

def customer_details(request):
     return render(request,'adminz/user.html')

def customer_profile(request):
     cd=request.session['username']
     customers=customer.objects.get(email=cd)
     return render(request,'adminz/customer_profile.html',{'customers':customers})

def customer_add(request):
     if request.method=="POST":  #Pasrsing Parameters
          customer_cname=request.POST.get("c_name")
          customer_email=request.POST.get("e_mail")
          customer_contact=request.POST.get("mob_no")
          customer_passwrd=request.POST.get("pass")
          
          e=customer()
          
          e.cname=customer_cname
          e.email=customer_email
          e.contact=customer_contact
          e.passwrd=customer_passwrd

          e.save()
          messages.success(request,"Inserted Successfully...!")
          return redirect("/adminhome/customer_view")
     return render(request, "adminz/user.html")
   
def customer_view(request):
     customers=customer.objects.all()
     return render(request,"adminz/cust_view.html",{'customers':customers})

def customer_delete(request,customer_id):
     customers=customer.objects.get(id=customer_id)
     customers.delete()
     messages.success(request,"Deleted Successfully...!")
     return redirect("/adminhome/customer_view")

def customer_update(request,customer_id):
     customers=customer.objects.get(id=customer_id)
     return render(request,"adminz/customer_update.html",{'customers':customers})

def customer_edit(request,customer_id):
     if request.method=="POST":
          customer_cname=request.POST.get("c_name")
          customer_email=request.POST.get("e_mail")
          customer_contact=request.POST.get("mob_no")
          customer_passwrd=request.POST.get("pass")

          e=customer.objects.get(id=customer_id)

          e.cname=customer_cname
          e.email=customer_email
          e.contact=customer_contact
          e.passwrd=customer_passwrd

          e.save()
          messages.success(request,"Updated Successfully...!")
          return redirect ("/adminhome/customer_view/")

def driver(request):
     return render(request,'adminz/driver.html')

def driver_add(request):
     if request.method=="POST":  #Pasrsing Parameters 
          driver_dname=request.POST.get("dname")
          driver_email=request.POST.get("email")
          driver_passw=request.POST.get("passd")
          driver_contact=request.POST.get("mobno")
          driver_auto_number=request.POST.get("anumber")
          driver_auto_type=request.POST.get("atype")
          driver_auto_date=request.POST.get("adate")
          driver_license_no=request.POST.get("lnumber")
          driver_auto_photo=request.FILES["aphoto"]
          driver_driver_photo=request.FILES["dphoto"]
          driver_driver_qr=request.FILES["dqr"]

          d=driverz()
          
          d.dname=driver_dname
          d.email=driver_email
          d.passw=driver_passw
          d.contact=driver_contact
          d.auto_number=driver_auto_number
          d.auto_type=driver_auto_type
          d.auto_date=driver_auto_date
          d.license_no=driver_license_no
          d.auto_photo=driver_auto_photo
          d.driver_photo=driver_driver_photo
          d.driver_qr=driver_driver_qr

          d.save()
          messages.success(request,"Inserted Successfully...!")
          return redirect("/adminhome/drivers_view")
     return render(request, "adminz/driver.html")

def drivers_view(request):
     drivers=driverz.objects.all()
     return render(request,"adminz/driver_view.html",{'drivers':drivers})

def driver_delete(request,driver_id):
     drivers=driverz.objects.get(id=driver_id)
     drivers.delete()
     messages.success(request,"Deleted Successfully")
     return redirect("/adminhome/drivers_view")

def driver_update(request,driver_id):
     drivers=driverz.objects.get(id=driver_id)
     return render(request,"adminz/driver_update.html",{'drivers':drivers})

def driver_profile(request):
     driver_id=request.session['drivername']
     drivers=driverz.objects.get(email=driver_id)
     return render(request,"adminz/driver_profile.html",{'drivers':drivers})

def driver_edit(request,driver_id):
     if request.method=="POST":  #Pasrsing Parameters 
          driver_dname=request.POST.get("dname")
          driver_email=request.POST.get("email")
          driver_contact=request.POST.get("mobno")
          driver_auto_number=request.POST.get("anumber")
          driver_auto_type=request.POST.get("atype")
          driver_auto_date=request.POST.get("adate")
          driver_license_no=request.POST.get("lnumber")
          driver_auto_photo=request.POST.get("aphoto")
          driver_driver_photo=request.POST.get("dphoto")
          driver_driver_qr=request.FILES["dqr"]

          d=driverz.objects.get(id=driver_id)
          
          d.dname=driver_dname
          d.email=driver_email
          d.contact=driver_contact
          d.auto_number=driver_auto_number
          d.auto_type=driver_auto_type
          d.auto_date=driver_auto_date
          d.license_no=driver_license_no
          d.auto_photo=driver_auto_photo
          d.driver_photo=driver_driver_photo
          d.driver_qr=driver_driver_qr

          d.save()
          messages.success(request,"Updated Successfully...!")
          return redirect ("/adminhome/drivers_view")

def ridebook(request,dr_id):
     dd=datetime.datetime.now()
     return render(request,'adminz/ride_book.html',{'customers':customer.objects.all(),'srv':driverz.objects.filter(id=dr_id),'dd':dd})

def ridebook_add(request):
     if request.method=="POST":  #Pasrsing Parameters
          ridecid=request.POST.get("zid")
          c_id=customer.objects.get(id=ridecid)  
          ride_book_did=request.POST.get("cid")
          d_id=driverz.objects.get(id=ride_book_did)
          ride_book_froute=request.POST.get("froute")
          ride_book_troute=request.POST.get("troute")
          ride_book_total_km=request.POST.get("tkm")
          ride_book_perkm_cost=request.POST.get("pcost")
          ride_book_total_amount=request.POST.get("tamount")
          ride_book_book_date=request.POST.get("bdate")
          ride_book_book_time=request.POST.get("btime")
          ride_book_book_status=request.POST.get("bstatus")

          rb=ride_book()
          
          rb.cid=c_id
          rb.did=d_id
          rb.froute=ride_book_froute
          rb.troute=ride_book_troute
          rb.total_km=ride_book_total_km
          rb.perkm_cost=ride_book_perkm_cost
          rb.total_amount=ride_book_total_amount
          rb.book_date=ride_book_book_date
          rb.book_time=ride_book_book_time
          rb.book_status=ride_book_book_status

          rb.save()
          messages.success(request,"Inserted Successfully...!")
          return redirect("/adminhome/ridebook_view") 
     return render(request,"adminz/ride_book.html")

def ridebook_view(request):
     ridebooks=ride_book.objects.all()
     return render(request,"adminz/ride_book_view.html",{'ridebooks':ridebooks})

def ridebook_delete(request,ridebook_id):
     ridebooks=ride_book.objects.get(id=ridebook_id)
     ridebooks.delete()
     messages.success(request,"Deleted Successfully...!")
     return redirect("/adminhome/ridebook_view")

def ridebook_update(request,ridebook_id):
     ridebooks=ride_book.objects.get(id=ridebook_id)
     return render(request,"adminz/ride_book_update.html",{'ridebooks':ridebooks,'customers':customer.objects.all(),'drv':driverz.objects.all()})

def ridebook_edit(request,ridebook_id):
     if request.method=="POST":  #Pasrsing Parameters
          ridecid=request.POST.get("zid")
          c_id=customer.objects.get(id=ridecid)  
          ride_book_did=request.POST.get("cid")
          d_id=driverz.objects.get(id=ride_book_did)
          ride_book_froute=request.POST.get("froute")
          ride_book_troute=request.POST.get("troute")
          ride_book_total_km=request.POST.get("tkm")
          ride_book_perkm_cost=request.POST.get("pcost")
          ride_book_total_amount=request.POST.get("tamount")
          ride_book_book_date=request.POST.get("bdate")
          ride_book_book_time=request.POST.get("btime")
          ride_book_book_status=request.POST.get("bstatus")

          rb=ride_book.objects.get(id=ridebook_id)

          rb.cid=c_id
          rb.did=d_id
          rb.froute=ride_book_froute
          rb.troute=ride_book_troute
          rb.total_km=ride_book_total_km
          rb.perkm_cost=ride_book_perkm_cost
          rb.total_amount=ride_book_total_amount
          rb.book_date=ride_book_book_date
          rb.book_time=ride_book_book_time
          rb.book_status=ride_book_book_status

          rb.save()
          messages.success(request,"Updated Successfully...!")
          return redirect("/adminhome/driveridebook")

def routes1(request):
     return render(request,'adminz/route.html')

def routes_add(request):
     if request.method=="POST":  #Pasrsing Parameters
          routes_froute=request.POST.get("f_route")
          routes_troute=request.POST.get("t_route")
          
          ro=routes()
          
          ro.froute=routes_froute
          ro.troute=routes_troute
          
          ro.save()
          messages.success(request,"Inserted Successfully...!")
          return redirect("/adminhome/routes_view")
     return render(request,"adminz/route.html")

def routes_view(request):
     routs=routes.objects.all()
     return render(request,"adminz/route_view.html",{'routs':routs})

def routes_delete(request,rout_id):
     routs=routes.objects.get(id=rout_id)
     routs.delete()
     messages.success(request,"Deleted Successfully...!")
     return redirect("/adminhome/routes_view")

def routes_update(request,rout_id):
     routs=routes.objects.get(id=rout_id)
     return render(request,"adminz/route_update.html",{'routs':routs})

def routes_edit(request,rout_id):
      if request.method=="POST":  #Pasrsing Parameters
          routes_froute=request.POST.get("f_route")
          routes_troute=request.POST.get("t_route")

          ro=routes.objects.get(id=rout_id)
          ro.froute=routes_froute
          ro.troute=routes_troute
          
          ro.save()
          messages.success(request,"Updated Successfully...!")
          return redirect("/adminhome/routes_view")

def payment1(request,ridebook_id):
     ridebooks=ride_book.objects.get(id=ridebook_id)
     return render(request,"adminz/payment.html",{'ridebooks':ridebooks})
     
def payment_add(request):
     if request.method=="POST":  #Pasrsing Parameters
          rbid=request.POST.get("rid")
          rb=ride_book.objects.get(id=rbid)
          driver_id=request.POST.get("driver_id")
          did=driverz.objects.get(id=driver_id)
          customer_id=request.POST.get("customer_id")
          cid=customer.objects.get(id=customer_id)
          ttype=request.POST.get("ttype")
          tamount=request.POST.get("tamount")
          tdate=request.POST.get("tdate")
          tstatus=request.POST.get("tstatus")
          rb=ride_book.objects.get(id=rbid)
          rb.book_status=tstatus

          rb.save()

          p=payment()
          
          p.rbook_id=rb
          p.did=did
          p.cid=cid
          p.t_type=ttype
          p.t_amount=tamount
          p.t_date=tdate
          p.pmtstatus=tstatus
          
          p.save()
          messages.success(request,"Payment Made Successfully...!")
          return redirect("/adminhome/driverpage")
     return render(request, "adminz/payment.html")

def payment_view(request):
     pay=payment.objects.all()
     return render(request,"adminz/payment_view.html",{'pay':pay})

def vehical(request):
     return render(request,"adminz/vehicle_location.html",{'drv':driverz.objects.all()})

def vehical_location_add(request):
     if request.method=="POST":  #Pasrsing Parameters
          dids=request.POST.get("vid")
          d_id=driverz.objects.get(id=dids)
          zipc=request.POST.get("zip")
          cit=request.POST.get("cit")
          coun=request.POST.get("con")
          addr=request.POST.get("addre")
          map_location=request.POST.get("map_location")
          
          vl=vehical_location()
          
          vl.did=d_id
          vl.zipcode=zipc
          vl.city=cit
          vl.country=coun
          vl.adress=addr
          vl.map_location=map_location
     
          vl.save()
          messages.success(request,"Inserted Successfully...!")
          return redirect("/adminhome/vehical_location_view")
     return render(request,"adminz/vehicle_location.html")

def vehical_location_view(request):
     vehl=vehical_location.objects.all()
     return render(request,"adminz/vehicle_view.html",{'vehl':vehl})

def vehical_location_delete(request,v_id):
     vehl=vehical_location.objects.get(id=v_id)
     vehl.delete()
     messages.success(request,"Deleted Successfully...!")
     return redirect("/adminhome/vehical_location_view")

def vehical_location_update(request,v_id):
     vehl=vehical_location.objects.get(id=v_id)
     return render(request,"adminz/vehicle_update.html",{'vehl':vehl,'drv':driverz.objects.all()})

def vehical_location_edit(request,v_id):
     if request.method=="POST":  #Pasrsing Parameters
          dids=request.POST.get("vid")
          d_id=driverz.objects.get(id=dids)
          zipc=request.POST.get("zip")
          cit=request.POST.get("cit")
          coun=request.POST.get("con")
          addr=request.POST.get("addre")
          map_location=request.POST.get("map_location")
          
          vl=vehical_location.objects.get(id=v_id)

          vl.did=d_id
          vl.zipcode=zipc
          vl.city=cit
          vl.country=coun
          vl.adress=addr
          vl.map_location=map_location
     
          vl.save()
          messages.success(request,"Updated Successfully...!")
          return redirect("/adminhome/vehical_location_view")



