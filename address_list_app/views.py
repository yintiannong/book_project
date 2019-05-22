from datetime import datetime
import datetime
from django.db.models import Model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import re
# Create your views here.

#收货地址界面：
from address_list_app.models import TAddress, TUser, TOrderitem, TOrder
from shopping_car_app.car_method import Book, Car
from shopping_car_app.models import TBook

def selects(request):
    val1=request.POST.get('val1')
    objects=TAddress.objects.get(address=val1)
    def mydefault(d):
        if isinstance(d,Model):
            print(122455)
            d_dict = d.__dict__
            d_dict.pop('_state')
            print(d.__dict__)
            return d_dict
    print(objects)
    return JsonResponse({'objects':objects},json_dumps_params={"default":mydefault})

def address_page(request):
    username=request.session.get('username')
    userid=TUser.objects.get(email=username).id
    print(userid)
    list11=TAddress.objects.filter(user_id=userid)
    print(list11)
    return render(request,'address/indent.html',{'list11':list11})

def receiver(request):
    rule='^[1-9]\d{5}$'
    val1=request.POST.get('val1')
    a=re.findall(rule,val1)
    if not val1:
        return HttpResponse('kong')
    else:
        if not a:
            return HttpResponse('error')
        else:
            return HttpResponse('ok')
def check_phone(request):
    rule='1[35678]\d{9}'
    val1=request.POST.get('val1')
    a=re.findall(rule,val1)
    if not val1:
        return HttpResponse('kong')
    else:
        if not a:
            return HttpResponse('error')
        else:
            return HttpResponse('ok')


#放回购物车
# def put_off(request):
#     car22=request.session.get('car')
#     bookid=request.POST.get('bookid')
#     print(car22.total_price,car22.list1)
#     for i in car22.list1:
#         print(i.book.id)
#         if i.book.id==int(bookid):
#
#             car22.list1.remove(i)
#     def mydefault(d):  # d = 需要转换格式的数据 = user
#         if isinstance(d,Book):
#             return d.__dict__
#         if isinstance(d, datetime):  # 判断是否为日期数据
#             # 返回格式化的数据
#             return d.strftime("%Y/%m/%d")
#         if isinstance(d,TBook):
#             return d.__dict__
#         if isinstance(d,Car):
#             return d.__dict__
#     print(car22.total_price,car22.list1)
#     return JsonResponse({'car2':car22}, json_dumps_params={"default":mydefault})
def submit_order(request):
    #获得用户的id
    username=request.session.get('username')
    userid=TUser.objects.get(email=username).id
    #获得姓名，地址，邮编，电话
    name=request.POST.get('name')
    address_1=request.POST.get('country_id')
    address_2=request.POST.get('province_id')
    address_3=request.POST.get('city_id')
    address_4=request.POST.get('town_id')
    address_5=request.POST.get('quarter_id')
    address_0=request.POST.get('address0')
    address=address_1+address_2+address_3+address_4+address_5+address_0
    zip_code=request.POST.get('zip_code')
    phone=request.POST.get('phone')
    #查看是否有满足这四个条件的
    a=TAddress.objects.filter(name=name,zip_code=zip_code,phone=phone)
    #如果没有，存库
    if not a:
        TAddress.objects.create(address=address,user_id=userid,name=name,zip_code=zip_code,phone=phone)
    #获得购物车
    car=request.session.get('car')

    address_id=TAddress.objects.get(name=name,zip_code=zip_code,phone=phone).id
    num = str(address_id) + '1264517'+str(userid)
    print(num,'num')
    TOrder.objects.create(num=num,create_time=datetime.datetime.now(),total_price=car.total_price,user_id=userid,address_id=address_id)
    list888=TOrder.objects.filter(user_id=userid)
    orderid=list888[len(list888)-1].id
    for i in car.list1:
        TOrderitem.objects.create(book_total=i.amount,xiaoji=i.per_total_price,book_id=i.book.id,order_id=orderid)
        #产品总数：
    sum=0
    for k in TOrderitem.objects.filter(order_id=orderid):
        sum+=int(k.book_total)
    del request.session['car']
    return render(request,'address/indent ok.html',{'num':num,'name':name,'total':sum,'price':car.total_price})


def login_out(request):
    del request.session['username']
    return redirect('book_fl:sy')
