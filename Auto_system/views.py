from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.contrib import messages
from auto_admin.models import *


def captcha(request):
    return render(request,'Captchapage.html')

def logotp(request):
    return render(request,'otplog.html')

def home(request):
    return render(request,'index1.html')

def signup(request):
    if request.method=="POST":  #Pasrsing Parameters
          customer_cname=request.POST.get("cname")
          customer_email=request.POST.get("email")
          customer_contact=request.POST.get("contact")
          customer_passwrd=request.POST.get("passwrd")
          
          e=customer()
          
          e.cname=customer_cname
          e.email=customer_email
          e.contact=customer_contact
          e.passwrd=customer_passwrd
          
          if customer.objects.filter(email=customer_email).exists():
            messages.success(request,"Already Email id exists..!")
            return redirect("/signup/")
          else:
           e.save()
           messages.success(request,"Registered Successfully! U can login now..")
          
           return redirect("/signin/")
    return render(request,'register.html')
        
def signin(request):
    if request.method == 'POST':
        usname = request.POST.get('email')
        passd = request.POST.get('pass')
        cen=request.POST.get('cen')
        cread=request.POST.get('cread')
        if cen!=cread:
          messages.error(request,"captcha mismatched!")
        else:

        #user = authenticate(request, username=usname, password=passd)
          usrs=customer.objects.filter(email=usname,passwrd=passd).count()
          if usrs > 0:
            usrs=customer.objects.filter(email=usname,passwrd=passd).first()
            messages.success(request,"Successfully logged in!")
            request.session['user_session']=True
            request.session['username']=usname
            request.session['userid']=usrs.id
            return redirect("/adminhome/adminpage/")
          else:
            messages.error(request,"Login failed due to invalid username or password")
    return render(request, 'logg.html')

     
def driverlogin(request):
    if request.method == 'POST':
        usname = request.POST.get('email')
        passd = request.POST.get('pass')
        cen=request.POST.get('cen')
        cread=request.POST.get('cread')
        if cen!=cread:
          messages.error(request,"captcha mismatched!")
        else:

        #user = authenticate(request, username=usname, password=passd)
          drv=driverz.objects.filter(email=usname,passw=passd).count()
          if drv > 0:
            drv=driverz.objects.filter(email=usname,passw=passd).first()
            messages.success(request,"Successfully logged in!")
            request.session['driver_session']=True
            request.session['drivername']=usname
            request.session['driver_id']=drv.id
            return redirect("/adminhome/driverhome/")
          else:
            messages.error(request,"Login failed due to invalid username or password")
    return render(request, 'driverlog.html')

def driveregister(request):
    if request.method=="POST":  #Pasrsing Parameters 
          driver_dname=request.POST.get("dname")
          driver_email=request.POST.get("email")
          driver_pass=request.POST.get("passw")
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
          d.passw=driver_pass
          d.contact=driver_contact
          d.auto_number=driver_auto_number
          d.auto_type=driver_auto_type
          d.auto_date=driver_auto_date
          d.license_no=driver_license_no
          d.auto_photo=driver_auto_photo
          d.driver_photo=driver_driver_photo
          d.driver_qr=driver_driver_qr

          if driverz.objects.filter(email=driver_email).exists():
            messages.success(request,"Already Email id exists..!")
            return redirect("/driveregister/")
          else:

           d.save()
           messages.success(request,"Registered Successfully! U can login now..")
          
          return redirect("/driverlogin/")
    return render(request,'driveregister.html')

def forget(request):
    return render(request,'forgot.html')

def logout(request):
    del request.session['user_session']
    return redirect('/signin/')
  
def dlogout(request):
    del request.session['driver_session']
    return redirect('/driverlogin/')
  
def changecpin(request):
  userid=request.session['userid']
  if request.method=="POST":
    op=request.POST.get("op")
    np=request.POST.get("np")
    cp=request.POST.get("cp")
    if customer.objects.filter(id=userid,passwrd=op) and np==cp:
      e=customer.objects.get(id=userid)
      e.passwrd=np
      e.save()
      messages.success(request,"Password changed successfully")
    else:
       errormessage="Invalid credentials"
       return render(request,"adminz/change_password.html",{'msg':errormessage})
  return render(request,"adminz/change_password.html")

def dchangecpin(request):
  driver_id=request.session['driver_id']
  if request.method=="POST":
    op=request.POST.get("op")
    np=request.POST.get("np")
    cp=request.POST.get("cp")
    if driverz.objects.filter(id=driver_id,passw=op) and np==cp:
      d=driverz.objects.get(id=driver_id)
      d.passw=np
      d.save()
      messages.success(request,"Password changed successfully")
    else:
       errormessage="Invalid credentials"
       return render(request,"adminz/driverchange_password.html",{'msg':errormessage})
  return render(request,"adminz/driverchange_password.html")


  


