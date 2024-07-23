from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30,blank=False)
    phone = models.CharField(max_length=11,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    message = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.email

class Reservation(models.Model):

    First_Name = models.CharField(max_length=30,blank=False)
    Last_Name = models.CharField(max_length=30,blank=False)
    Phone = models.CharField(max_length=11,blank=False)
    Email = models.EmailField(max_length=50,blank=False)
    Date = models.DateField(null=True)
    person = models.IntegerField(max_length=2,null=True)
    hour = models.CharField(max_length=5,default="9.00")

    def __str__(self):
        return self.Email
