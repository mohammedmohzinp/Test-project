from django.conf.urls import url
from django.urls import path, re_path
from .views import *


urlpatterns=[

    url('uploaddepartment', uploaddepartment, name='uploaddepartment'),
    url('viewdepartment', viewdepartment, name='viewdepartment'),
    url('deleteDeparment', deleteDeparment, name='deleteDeparment'),
    url('updateDeparment', updateDeparment, name='updateDeparment'),
    
    



]