from django.shortcuts import render,redirect
from hashlib import sha256
from django.contrib.auth.models import User,auth

from .models import *
# from django.contrib.messages import get_messages
from django.contrib import messages
# Create your views here.


def signup(request):
	if request.method == 'POST':

		username	= request.POST.get("username")
		phone		= request.POST.get("phone")
		dateofbirth = request.POST.get("dateofbirth")
		password	= request.POST.get("password")
		profile		= request.POST.get("profile")
		role		= request.POST.get("role")

		print(username,phone,dateofbirth,profile,role)

		adminStatus	= False
		if role == 'admin':
			adminStatus	= True

		already_exist	= User.objects.filter(username=phone)
		print(already_exist)
		if already_exist:

			print("This user already_exist")
			messages.error(request, "User already_exist")
			return redirect('signup')

		else:
			user 	= User.objects.create_user(username=phone, password=password,is_superuser=adminStatus)
			user.save()

			otherDetails	= extendedUser()
			otherDetails.user		= User.objects.get(username=phone)
			otherDetails.username	= username
			otherDetails.phone 		= phone
			otherDetails.dateofbirth= dateofbirth
			otherDetails.profile	= profile
			otherDetails.userType	= role
			otherDetails.save()
			# messages.success(request, 'Registration successful')

			return redirect('login')



	else:
		return render(request,'signup.html')



def login(request):
	if request.method == 'POST':
		phone		= request.POST.get("phone")
		password	= request.POST.get("password")

		check_user	= User.objects.filter(username=phone)
		if check_user:

			user 	= auth.authenticate(username=phone,password=password)
			if user is not None:
				auth.login(request,user)
				user_id		= request.session['id'] = user.id
				print(user_id)
				check_user 	= extendedUser.objects.get(user=user)
				if check_user.userType == 'admin':
					# return render(request,'admin/admin.html')
					return redirect('/area_admin/admin_home')

				else:

					return redirect('/student/student_home')
					
			else:
				messages.error(request,'Invalid User')
				return redirect('login')
			
		else:
			messages.error(request, "Check Your credential")
			return redirect('login')


	else:
		return render(request,'login.html')