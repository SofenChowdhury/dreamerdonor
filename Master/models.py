from django.db import models

# Create your models here.
class Master(models.Model):

	title 		= models.CharField(max_length=200, default='Dreamer & Donor',blank=True)
	logo 		= models.ImageField(upload_to='assets/uploads/setup',blank=True)
	fb 			= models.CharField(max_length=200,blank=True)
	youtube		= models.CharField(max_length=200,blank=True)
	insta		= models.CharField(max_length=200,blank=True)
	phone		= models.CharField(max_length=50,blank=True)
	email		= models.EmailField(max_length=200,blank=True)
	address		= models.CharField(max_length=300,blank=True)
	city		= models.CharField(max_length=50,blank=True)
	country		= models.CharField(max_length=100,blank=True)
	start_time	= models.TimeField(default='10:00:00',blank=True)
	end_time	= models.TimeField(default='18:00:00',blank=True)

	def __str__(self):
		return self.title
	class Meta:
	    verbose_name_plural = "Contact Us"
class TermsCondition(models.Model):
	title 	= models.CharField(max_length=200)
	description 	= models.TextField(blank=True,null=True)
	def __str__(self):
		return self.title

	class Meta:
	    verbose_name_plural = "Terms & Conditions"

class AboutUs(models.Model):
	title 			= models.CharField(max_length=200)
	image 			= models.ImageField(upload_to='assets/uploads/setup',blank=True,null=True)
	description 	= models.TextField(blank=True,null=True)
	def __str__(self):
		return self.title

	class Meta:
	    verbose_name_plural = "About Us"

class Companyinfo(models.Model):
	title 			= models.CharField(max_length=200)
	image 			= models.ImageField(upload_to='assets/uploads/setup',blank=True,null=True)
	video_link 		= models.TextField(blank=True,null=True)
	description 	= models.TextField(blank=True,null=True)
	def __str__(self):
		return self.title

	class Meta:
	    verbose_name_plural = "Company Info"