from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', signin, name='login'),
    url(r'^loginin/$', login_, name='login_in'),
    url(r'^registerin/$', register_, name='register_in'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^buyinfo/$',buyinfo,name='buyinfo'),
    url(r'^infomes/$',infomes_,name='infomes_in'),
    url(r'^service$',service,name='service'),
]