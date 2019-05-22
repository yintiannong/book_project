from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from shopping_car_app.car_method import Car




#展示购物车主界面
from shopping_car_app.models import TBook


def shopp_car_page(request):
    car=request.session.get('car')
    if not car:
        car=Car()
    objects=car.list1
    #包含着书的对象和本数
    lens = len(car.list1)
    return render(request,'shopping_car/car.html',{'objects':objects,'lens':lens})


def add(request):
    #添加商品
    bookid=request.GET.get('bookid')

    amount=request.GET.get('amount1')
    print(bookid,amount)
    car=request.session.get('car')

    if car:
        car.add_mark(int(bookid),int(amount))
    else:
        car=Car()
        car.add_mark(int(bookid),int(amount))
    request.session['car'] = car
    return HttpResponse('niubi')
def change(request):
    #修改购物车
    bookid=int(request.GET.get('bookid'))
    amount=request.GET.get('amount')
    amount=int(amount)
    car=request.session.get('car')
    car.change_car(bookid,amount)
    request.session['car']=car
    print(bookid)
    book=int(TBook.objects.get(id=int(bookid)).dangdang_price)*int(amount)
    nong={'per_book_price':book,'zong':car.total_price,'cha':car.mark}
    return JsonResponse(nong)

def del_goods(request): #删除商品
    bookid=request.GET.get('bookid')
    car=request.session.get('car')
    car.del_car(bookid)
    request.session['car']=car
    lens=len(car.list1)
    nong = {'zong': car.total_price, 'cha': car.mark,'lens':lens}
    return JsonResponse(nong)
def huifu_goods(request):

    bookid=request.GET.get('bookid')
    amount=request.GET.get('amount1')
    car=request.session.get('car')
    car.huifu_car(int(bookid),int(amount))
    request.session['car']=car
    car=request.session.get('car')
    print(car.total_price)
    return redirect('gwc:gwc_page')




#结算点击——>未登录跳转至登录，登录时跳转至填写地址界面
def settlement(request):
    username=request.session.get('username')
    if username:
        return redirect('dz:dz')
    else:
        request.session['car2']='123'
        return redirect('yh:dljm')