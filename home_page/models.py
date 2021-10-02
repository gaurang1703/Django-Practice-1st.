from django.db import models

# Create your models here.


class contactus(models.Model):
    name = models.CharField(max_length=150)

    email = models.CharField(max_length=120)
    pincode = models.CharField(max_length=10)
    mobile = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics")
    suggestions = models.CharField(max_length=500)
    def __str__(self):
        return(self.name)


class destinations(models.Model):
    name= models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    details=models.CharField(max_length=200)
    image=models.ImageField(upload_to='destinations')

    def __str__(self):
        return(self.name)
   


class student():
    name = str
    address = str
    mobile = str
    pincode = str
    standard = str
    ispass = bool
