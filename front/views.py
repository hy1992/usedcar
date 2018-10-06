import random
import logging
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from sale.models import *


def index(request):
    brand = request.GET.get('brand',None)
    if brand == None:
        try:
            car_list = Carinfo.objects.filter(isPurchase=False,isDelete=False)
            car_five = random.sample(list(car_list),5)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            logging.warning(e)
    else:
        brand = Brand.objects.get(btitle=brand)
    return render(request,'index.html',{'carlist':locals()})


