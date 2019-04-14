from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	fname=models.CharField(max_length=100, default='')
	lname=models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	dob = models.DateField(blank=True,null=True,verbose_name="dob")

	def __str__(self):
		return self.user.username

class HospitalProfileInfo(models.Model):
	h_user=models.OneToOneField(User, on_delete=models.CASCADE)
	h_name=models.CharField(max_length=100, default='')
	h_city=models.CharField(max_length=100, default='')
	h_address=models.TextField(max_length=200,default='')

	def __str__(self):
		return self.h_user.username

class PharmacyProfileInfo(models.Model):
	p_user= models.OneToOneField(User, on_delete=models.CASCADE)
	p_name= models.CharField(max_length=100, default='')
	p_city=models.CharField(max_length=100, default='')
	p_address=models.TextField(max_length=200,default='')

	def __str__(self):
		return self.p_user.username

class Outbreak(models.Model):
	disease_name =models.CharField(max_length=100,default='')
	no_of_deaths = models.IntegerField(default=0)
	no_of_affected = models.IntegerField(default=0)
	location = models.CharField(max_length=100,default='')
	date = models.DateField(verbose_name="date")

	def __str__(self):
		return self.disease_name




