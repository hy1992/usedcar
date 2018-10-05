from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'protection',protection,name='protection'),
    url(r'detail',detail_one,name='buydetailone'),
    url(r'price',price,name='price'),
]