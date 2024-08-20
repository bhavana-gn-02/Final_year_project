
from django.db import models

# Create your models here.
class customer(models.Model):
    cname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    contact=models.CharField(max_length=50)
    passwrd=models.CharField(max_length=200)
    def __str__(self):
        return self.cname

class driverz(models.Model):
    dname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    passw=models.CharField(max_length=200)
    contact=models.CharField(max_length=50)
    auto_number=models.CharField(max_length=200)
    auto_type=models.CharField(max_length=200)
    auto_date=models.CharField(max_length=200)
    license_no=models.CharField(max_length=200)
    auto_photo=models.FileField(upload_to="images/",max_length=250,null=True,default=None)
    driver_photo=models.FileField(upload_to="images/",max_length=250,null=True,default=None)
    driver_qr=models.FileField(upload_to="images/",max_length=250,null=True,default=None)
    
    def __str__(self):
        return self.dname


class routes(models.Model):
    froute=models.CharField(max_length=200)
    troute=models.CharField(max_length=200)

class ride_book(models.Model):
    cid=models.ForeignKey(customer,on_delete=models.CASCADE)
    did=models.ForeignKey(driverz,on_delete=models.CASCADE)
    froute=models.CharField(max_length=200)
    troute=models.CharField(max_length=200)
    total_km=models.CharField(max_length=200)
    perkm_cost=models.CharField(max_length=150)
    total_amount=models.CharField(max_length=150)
    book_date=models.CharField(max_length=200)
    book_time=models.CharField(max_length=150)
    book_status=models.CharField(max_length=150)
    
    @property
    def driver_qr(self):
        return self.did.driver_qr

class payment(models.Model):
    rbook_id=models.ForeignKey(ride_book,on_delete=models.CASCADE)
    did=models.ForeignKey(driverz,on_delete=models.CASCADE)
    cid=models.ForeignKey(customer,on_delete=models.CASCADE)
    t_type=models.CharField(max_length=150,null=True,default=None)
    t_amount=models.CharField(max_length=150)
    t_date=models.CharField(max_length=150)
    pmtstatus=models.CharField(max_length=150)
    
    

class vehical_location(models.Model):
    did=models.ForeignKey(driverz,on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    map_location = models.CharField(max_length=400,blank=True, null=True)
    
    @property
    def driver_photo(self):
        return self.did.driver_photo
