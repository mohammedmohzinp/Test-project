from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK

)
from django.http import JsonResponse
import json
import requests
from django.db.models import QuerySet
from django.core import serializers
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User,auth
from rest_framework.response import Response
from .models import *
from student.models import *

# Create your views here.




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def uploaddepartment(request):
	department_dt  = request.data.get("department")
	icon        = request.FILES.get("image")
	# status      = request.data.get("status")
	print(department_dt)
	check_exist = Department.objects.filter(Department=department_dt)
	print(check_exist)
	if check_exist:
		return Response({"code": "422", "message": "Data alredy Exist in Database", "Response": False},status=HTTP_400_BAD_REQUEST)


	else:
		store_data  = Department()
		store_data.Department   = department_dt
		store_data.profile      = icon
		store_data.status       = True
		store_data.save()

		return Response({"code": "422", "message": "Success", "Response": False},status=HTTP_200_OK)






@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def viewdepartment(request):
	data    = Department.objects.filter(status=True)
	return JsonResponse(list(data.values()),safe=False)

	



@csrf_exempt
@api_view(["DELETE"])
@permission_classes((AllowAny,))
def deleteDeparment(request):
	dip_id  = request.data.get("departmentId")

	data    = Department.objects.get(id=dip_id)
	if data:
		data.delete()
		return Response({"code": "422", "message": "Success", "Response": False},status=HTTP_200_OK)

	else:
		return Response({"code": "422", "message": "error", "Response": False},status=HTTP_400_BAD_REQUEST)







@csrf_exempt
@api_view(["PUT"])
@permission_classes((AllowAny,))
def updateDeparment(request):
	dip_id  = request.data.get("departmentId")
	department_dt  = request.data.get("department")
	icon        = request.FILES.get("image")
	# status      = request.data.get("status")

	data    = Department.objects.get(id=dip_id)
	if data:
		data.Department = department_dt
		data.icon  = icon
		
		data.save()
		return Response({"code": "422", "message": "Success", "Response": False},status=HTTP_200_OK)

	else:
		return Response({"code": "422", "message": "error", "Response": False},status=HTTP_400_BAD_REQUEST)