from django.shortcuts import render
from .models import *
import random
import logging
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def protection(request):
    return render(request,'protection.html')

def detail_one(request):
    car_id = request.GET.get('carid')
    try:
        carone = Carinfo.objects.get(id=car_id)
    except ObjectDoesNotExist as e:
        logging.warning(e)
    if request.COOKIES.get('Recently_viewed',''):
        cookie_car = request.COOKIES.get('Recently_viewed')
        list_car = cookie_car.split(',')
        if car_id in list_car:
            list_car.remove(car_id)
        if len(list_car) >= 2:
            list_car.pop()
        list_car = [car_id] + list_car
        cookie_car_new = ','.join(list_car)
        response = render(request,'detail.html',{'carone':carone})
        response.set_cookie('Recently_viewed',cookie_car_new,max_age=3000)
        return response
    return render(request,'detail.html',{'carone':carone})

def price(request):
    brand = request.GET.get('brand',None)
    brandlist = Brand.objects.all().order_by('id')
    pri = request.GET.get('pri')
    if pri == '10':
        upprice = 10
        lowerprice = 0
    elif pri == '30':
        upprice = 30
        lowerprice = 10
    elif pri == '80':
        upprice = 80
        lowerprice = 30
    elif pri == '801':
        upprice = 801
        lowerprice = 80
    if brand == 'None':
        try:
            carlist = Carinfo.objects.filter(isPurchase=False,isDelete=False,extractprice__lt=upprice,extractprice__gte=lowerprice)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            logging.warning(e)
    else:
        try:
            carlist = Carinfo.objects.filter(isPurchase=False,isDelete=False,extractprice__lt=upprice,extractprice__gte=lowerprice)
            brand_id = Brand.objects.filter(btitle=brand)[0].id
        except ObjectDoesNotExist as e:
            logging.warning(e)
    return render(request,'list.html',{'carlist':locals()})

