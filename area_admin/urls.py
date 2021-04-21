from django.conf.urls import url
from django.urls import path, re_path
from .views import *


urlpatterns=[

    url('admin_home/', admin_home, name='admin_homepage'),
    url('admin_logout', admin_logout, name='admin_logout'),
    url('student_details', student_details, name='student_details'),
    url('editmark', editmark, name='editmark'),


    
    



]