from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'buylist',buylist,name='buylist'),
    url(r'brandlist',brandlist,name='brandlist'),
    url(r'userinfo',userinfo,name='userinfo'),
    url(r'addorder',add_order,name='addorder'),
    url(r'confirmbuy',confirmbuy,name='confirmbuy'),
    url(r'delcart',delcart,name='delcart'),
    url(r'alterinfo',alter_info,name='alter_info'),
    url(r'reoffer',reoffer,name='reoffer'),
    url(r'cancelorder',cancel_order,name='cancelorder'),
]