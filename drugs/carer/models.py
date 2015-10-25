from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	substance = models.CharField(max_length=30)
	lastMeeting = models.DateField()
	checkedIn = models.BooleanField()