import logging
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from sale.models import *
from .models import *
# Create your views here.
# 买车列表
def buylist(request):
    carlist = Carinfo.objects.filter(isPurchase=False,isDelete=False)[:8]
    brandlist = Brand.objects.all().order_by('id')
    return render(request,'list.html',{'carlist':locals()})
# 车辆品牌列表
def brandlist(request):
    btitle = request.GET.get('brand')
    try:
        brand = Brand.objects.get(btitle=btitle)
        carlist = brand.carinfo_set.filter(isPurchase=False,isDelete=False)
        brandlist = Brand.objects.all().order_by('id')
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return render(request,'list.html',{'carlist':locals()})

# 添加购买
def add_order(request):
    if request.user.is_authenticated():
        car_id = request.GET.get('carid')
        try:
            car_ = Carinfo.objects.get(id=car_id)
            brand = str(car_.serbran) + car_.ctitle
            picture = car_.picture
            price = car_.extractprice
            newprice = car_.newprice
            mileage = car_.mileage
            Cart.objects.create(suser=request.user,car=car_,brand=brand,picture=picture,price=price,newprice=newprice,mileage=mileage)
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return render(request,'order.html',{'car':locals()})
    else:
        return redirect('/user/login/')

# 确认购买
def confirmbuy(request):
    if request.user.is_authenticated():
        car_id = request.GET.get('carid')
        orderNo = datetime.datetime.now().strftime('%Y%m%m%H%M%S')
        try:
            car_ = Cart.objects.filter(car_id=car_id)
            car = Carinfo.objects.filter(id=car_id)
            brand = car_[0].brand
            picture = car_[0].picture
            price = car_[0].price
            newprice = car_[0].newprice
            mileage = car_[0].mileage
            Orders.objects.create(sale_user=car[0].user,buy_user=request.user,brand=brand,picture=picture,price=price,newprice=newprice,mileage=mileage,orderNo=orderNo)
            Carinfo.objects.filter(id=car_id).update(isPurchase=True)
        except ObjectDoesNotExist as e:
            logging.warning(e)
        # 最近浏览
        try:
            rec_view_list = list()
            if request.COOKIES.get('Recently_Viewed',None):
                rec_view = request.COOKIES.get('Recently_Viewed')
                list_view = rec_view.split(',')
                for i in list_view:
                    rec_view_list.append(Carinfo.objects.get(id=i))
            else:
                rec_view_list = []
        except ObjectDoesNotExist as e:
            logging.warning(e)

        user_id = request.user.id
        orders = Orders.objects.filter(id=user_id).order_by('id')[:4]
        user = UserInfo.objects.filter(id=user_id)[0]
        car = Carinfo.objects.filter(user_id=user_id,isPurchase=False)[:4]
        return render(request,'user-info.html',{'orders':locals()})
    else:
        return redirect('/user/login/')

# 取消订单
def delcart(request):
    if request.user.is_authenticated():
        user_id = request.user.id
        car_id = request.GET.get('carid')
        try:
            Cart.objects.filter(suser_id=user_id,car_id=car_id).delete()
        except BaseException as e:
            logging.warning(e)
        return redirect('/')
    else:
        return redirect('/user/login/')

# 个人中心
def userinfo(request):
    if request.user.is_authenticated():
        # 最近浏览
        try:
            rec_view_list = list()
            if request.COOKIES.get('Recently_Viewed', None):
                rec_view = request.COOKIES.get('Recently_Viewed')
                list_view = rec_view.split(',')
                for i in list_view:
                    rec_view_list.append(Carinfo.objects.get(id=i))
            else:
                rec_view_list = []
        except ObjectDoesNotExist as e:
            logging.warning(e)

        user_id = request.user.id
        orders = Orders.objects.filter(id=user_id).order_by('id')[:4]
        user = UserInfo.objects.filter(id=user_id)[0]
        car = Carinfo.objects.filter(user_id=user_id, isPurchase=False)[:4]
        return render(request, 'user-info.html', {'orders': locals()})
    else:
        return redirect('/user/login/')

# 个人信息修改
def alter_info(request):
    if request.method == 'POST':
        realname = request.POST.get('name')
        sex = request.POST.get('sex')
        if sex == '男':
            sex = '0'
        elif sex == '女':
            sex = '1'
        else:
            print("性别错误")
        phone = request.POST.get('phone')
        userid = request.user.id
        UserInfo.objects.filter(id=userid).update(realname=realname,sex=sex,cellphone=phone)
        return redirect('/buy/userinfo')


# 取消卖车
def cancel_order(request):
    user_id = request.user.id
    car_id = request.GET.get('carid')
    try:
        Carinfo.objects.filter(user_id=user_id,id=car_id).update(isDelete=True)
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return redirect('/buy/userinfo/')

# 重新出价
def reoffer(request):
    if request.method == 'POST':
        user_id = request.user.id
        car_id = request.POST.get('carid')
        alterprice = request.POST.get('alterprice')
        extractprice = int(alterprice)*0.02 + int(alterprice)
        try:
            Carinfo.objects.filter(user_id=user_id, id=car_id).update(price=alterprice,extractprice=extractprice)
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return redirect('/buy/userinfo/')

