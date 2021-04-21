from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.



class Department(models.Model):
	Department 	= models.CharField(max_length=30)
	profile		= models.ImageField(upload_to="department")
	status		= models.BooleanField()
	date  		= models.DateTimeField(auto_now=True)


class Batch(models.Model):
	Department 	= models.ForeignKey(Department, on_delete=models.CASCADE)
	batch    	= models.CharField(max_length=30)
	profile		= models.ImageField(upload_to="batch")
	status		= models.BooleanField()
	date  		= models.DateTimeField(auto_now=True)



class studentDetails(models.Model):
	student 	= models.OneToOneField(User, on_delete=models.CASCADE)
	Institute 	= models.CharField(max_length=40)
	batch    	= models.ForeignKey(Batch, on_delete=models.CASCADE)
	department  = models.ForeignKey(Department, on_delete=models.CASCADE)
	location	= models.CharField(max_length=40)
	date  		= models.DateTimeField(auto_now=True)




class Subjects(models.Model):
    subjectCode  = models.CharField(max_length=30)
    Subject      = models.CharField(max_length=12)
    status		 = models.BooleanField()
    date     	 = models.DateTimeField(auto_now=True)



class StudentMarks(models.Model):
	student 	= models.OneToOneField(User, on_delete=models.CASCADE)
	subjectCode = models.ForeignKey(Subjects, on_delete=models.CASCADE)
	mark        = models.IntegerField()
	examdate    = models.DateTimeField(auto_now=True)
	date        = models.DateTimeField(auto_now=True)
