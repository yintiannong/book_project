from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from backstage_app.models import TBook, BookKind, TAddress, TOrder


def backstage_page(request):


    return render(request,'backstage/index.html')


def addbook_page(request):
    list777 = BookKind.objects.filter(parent_id__gt=0)
    return render(request,'backstage/add.html',{'list777':list777})
#添加书：
def addbook(request):
    bookname=request.POST.get('name')
    author=request.POST.get('author')
    publish=request.POST.get('publish')
    parent_name=int(request.POST.get('parent_kind'))
    create_date=request.POST.get('create_time')
    sales = request.POST.get('sales') #销量
    dang_price = request.POST.get('dang_price')
    market_price = request.POST.get('market_price')
    num_words = request.POST.get('num_words')
    recommend = request.POST.get('recommend')
    print_date = request.POST.get('print_date')
    parent_name = BookKind.objects.get(id=parent_name)
    TBook.objects.create(book_name=bookname,author=author,publish=publish,book_kind=parent_name,create_time=create_date,print_time=print_date,sales_volume=sales,dangdang_price=dang_price,mark_price=market_price,word_num=num_words,recommend=recommend)
    return redirect('ht:htjm')


def book_list_page(request):
    list_book=TBook.objects.filter()
    lens=len(list_book)
    return render(request,'backstage/list.html',{'list_book':list_book,'lens':lens})


def add_parent_kind_list_page(request):
    return render(request,'backstage/zjsp.html')
def add_parent(request):
    name=request.POST.get('nm')
    BookKind.objects.create(name=name)
    return redirect('ht:add_parent_page')



def add_parent_kind_list_page(request):
    return render(request,'backstage/zjsp.html')


def add_child_kind_list_page(request):
    a=BookKind.objects.filter()

    return render(request,'backstage/zjzlb.html',{'a':a})
def add_child(request):
    name=request.POST.get('name')
    parent_name=request.POST.get('parent_name')
    parent_id=BookKind.objects.get(name=parent_name).id
    BookKind.objects.create(name=name,parent_id=parent_id)
    return redirect('ht:add_child_page')


def book_kind_page(request):
    wudi=BookKind.objects.filter(parent_id__gt=0)
    return render(request,'backstage/splb.html',{'wudi':wudi})


def address_page(request):
    a=TAddress.objects.filter()
    return render(request,'backstage/dzlist.html',{'a':a})
def address_order_page(request):
    a=TOrder.objects.filter()
    return render(request,'backstage/order_list.html',{'a':a})


def dels(request):
    flag=request.GET.get('flag')
    if flag=='1':
        id=request.GET.get('id')
        a=TBook.objects.get(id=id)
        a.delete()
        return redirect('ht:book_list')
    if flag=='2':
        name=request.GET.get('name')
        print(name)
        a=BookKind.objects.get(name=name)
        a.delete()
        return redirect('ht:book_kind')
    if flag=='3':
        id=request.GET.get('id')
        print(id)
        for i in id.split(','):
            print(i)
            if i=='0':
                pass
            else:
                TOrder.objects.get(id=int(i)).delete()
        return HttpResponse('yes')
    if flag=='4':
        pass