from django.conf.urls import url
from django.urls import path, re_path
from .views import *


urlpatterns=[

    url('student_home/', student_home, name='student_home'),
    url('editstudent/', editstudent, name='editstudent'),
    url('update_user/', update_user, name='update_user'),
    


]