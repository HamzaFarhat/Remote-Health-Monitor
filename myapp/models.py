from django.db import models

# Create your models here.
class Vitals(models.Model):
	diastolic = models.CharField(max_length=200)
	systolic = models.CharField(max_length=200)
	heartRate = models.CharField(max_length=200)
	oxygenSaturation = models.CharField(max_length=200)
	
