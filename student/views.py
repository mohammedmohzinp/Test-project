from django.shortcuts import render,redirect
from registration.models import *
from student.models import *

# Create your views here.




def student_home(request):
	if request.session.has_key('id'):

		return render(request,'student/index.html')
	else:
		return redirect('/login')


def editstudent(request):
	if request.session.has_key('id'):

		if request.method == "POST":
			pass
		else:
			student_data=[]

			data	= extendedUser.objects.get(user_id=request.session['id'])
			if studentDetails.objects.filter(student_id=request.session['id']):
				student_data 	= studentDetails.objects.get(student_id=request.session['id'])

			return render(request,'student/editprofile.html',{"maindata":data,"second_data":student_data})
	else:
		return redirect('/login')



def update_user(request):
	if request.session.has_key('id'):

		if request.method == "POST":
			username = request.POST.get("username")
			phone 	=	request.POST.get("phone")
			dateofbith 	= request.POST.get("dateofbirth")
			photo 	= request.FILES.get('photo')

			insert = extendedUser.objects.get(user_id=request.session['id'])
			insert.username =username
			insert.phone  =	phone
			if dateofbith is not None:
				insert.dateofbirth =dateofbith
			if photo is not None:
				insert.profile = photo
			insert.save()
			return redirect('editstudent')
		else:
			student_data=[]

			data	= extendedUser.objects.get(user_id=request.session['id'])
			if studentDetails.objects.filter(student_id=request.session['id']):
				student_data 	= studentDetails.objects.get(student_id=request.session['id'])

			return render(request,'student/updateprofile.html',{"maindata":data,"second_data":student_data})
	else:
		return redirect('/login')