from django.shortcuts import render,redirect
from hashlib import sha256
from django.contrib.auth.models import User,auth
from registration.models import *
from .models import *
from student.models import *
from django.contrib import messages
# Create your views here.


def admin_home(request):
	if request.session.has_key('id'):
		print(request.user)
		all_users	= extendedUser.objects.all().exclude(user_id=request.session['id'])
		all_students	= extendedUser.objects.filter(userType='student')

		# context	= {""}

		return render(request,'admin/admin.html',{"all_users":all_users,"all_students":all_students})
	else:
		return redirect('/login')





def student_details(request):
	if request.session.has_key('id'):
		user_id	= request.GET.get("id")
		data = studentDetails.objects.filter(student_id=user_id)
		mark_details =[]
		print(data,user_id)
		if data:
			data = studentDetails.objects.get(student_id=user_id)
			mark_details = StudentMarks.objects.filter(student_id=user_id)
			print(mark_details)
			if mark_details:
				mark_data = StudentMarks.objects.filter(student_id=user_id)
				print("opps>>>",mark_data)

			return render(request,'admin/student_details.html',{"data":data,"mark_details":mark_data})



		else:
			messages.error(request,"Currently data Not avalilable")
			return render(request,'admin/student_details.html')

	else:
		return redirect('/login')








def editmark(request):
	if request.method == 'POST':
		id 	= request.POST.get("markid")
		print(id)

		new_mark = request.POST.get("mark")
		print(new_mark)
		stud_data 	= StudentMarks.objects.filter(id=id)

		if stud_data:
			data 	= StudentMarks.objects.get(id=id)
			data.mark = new_mark
			data.save()
			return redirect('/area_admin/admin_home')

		else:
			print("error")

	# else:
	# 	id 	= request.GET.get("id")







def admin_logout(request):
	auth.logout(request)
	try:
		del request.session['id']
	except:
		pass
	return redirect('login')