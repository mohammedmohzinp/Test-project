from django.conf.urls import url
from django.urls import path, re_path
from .views import *


urlpatterns=[

    # url('', homepage, name='homepage'),
    url('login/', login, name='login'),
    url('signup/', signup, name='signup'),


]