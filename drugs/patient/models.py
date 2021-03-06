from django.db import models

#patient details

class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True, primary_key=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20,default="")


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100)    

class Login(models.Model):
    username = models.ForeignKey(Patient, to_field="email",default="")
    password = models.CharField(max_length=20,default="")    


    substance = models.CharField(max_length=30)
    lastMeeting = models.DateField()
    checked_in = models.BooleanField()


# Create your models here.
