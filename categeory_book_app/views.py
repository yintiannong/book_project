from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from categeory_book_app.models import BookKind, TBook

#设计首页的信息
def home_page(request):
    dels=request.GET.get('dels')
    if  dels:
        del request.session['username']
    username=request.session.get('username')
    a = BookKind.objects.filter(parent_id=None) #调取一级目录
    b =BookKind.objects.filter(parent_id__gt=0) #调取二级目录
    c =TBook.objects.filter().order_by('-create_time')[0:8] #调取上架时间排序，传到模板中，可以选前八个
    d=TBook.objects.filter().order_by('-create_time').order_by('-sales_volume')[0:5]
    #最新上架的卖的做多的
    e=TBook.objects.filter(editor_recommendation=1)#编辑推荐
    if username:
        return render(request,'categeory_book/index.html',{'big':a,'small':b,'new_book':c,'sales_vloume':d,'tj':e,'username':username})

    else:
        return render(request, 'categeory_book/index.html',{'big': a, 'small': b, 'new_book': c, 'sales_vloume': d, 'tj': e})

#设计书详细信息的数据调取
def book(request):
    id=request.GET.get('id')
    book_information=TBook.objects.get(id=id) #书的基本信息
    a = BookKind.objects.filter(parent_id=None)  #一级目录
    return render(request,'book/Book details.html',{'book':book_information,'big':a},)


#跳转书的分类详情界面：
def book_list_page(request):
    dels = request.GET.get('dels')
    orderbys=request.GET.get('orderby')
    alls=TBook.objects.all()
    if not orderbys or orderbys=='0':
        alls=TBook.objects.all()     #默认排序
    elif orderbys=='1':
        alls=TBook.objects.all().order_by('-create_time')  #出版时间
    elif orderbys=='2':
        alls=TBook.objects.all().order_by('-sales_volume')  #销量
    elif orderbys=='3':
        alls=TBook.objects.all().order_by('dangdang_price') #当当价钱
    print(alls)
    a = BookKind.objects.filter(parent_id=None)  # 调取一级目录
    b = BookKind.objects.filter(parent_id__gt=0)  # 调取二级目录
    id = request.GET.get('id')  # 接受分类的id
    parent_id=request.GET.get('parent_id') #接受其父类的id
    print(parent_id)
    if parent_id!='None':
        list1=alls.filter(book_kind=id) #点击二级目录时的处理
    else:
        list1=[]                      #点击一级目录时的处理

        for i in alls:
            if i.book_kind.parent_id==int(id):
                list1.append(i)
    num=request.GET.get('num')
    if not num :
        num=1
    product_count=len(list1)
    page=Paginator(list1,per_page=5).page(num) #分页操作，把要传的东西，分为5个一页
    c=BookKind.objects.get(id=id)
    mu=request.GET.get('mu')
    if dels:
        del request.session['username']
    a = render(request, 'categeory_book/booklist.html',{'big': a, 'small': b, 'dict1': c, 'list1': page, 'id': id, 'parent_id': parent_id,'product_count': product_count, 'orderbys': orderbys, 'mu': mu})
    return a


