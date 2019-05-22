import datetime
import hashlib
import os
import random
import string
from urllib import response

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite1.settings'
# Create your views here.



#注册界面的进入


from captcha.image import ImageCaptcha

import re

from user_app.models import TUser


def regist_page(request):
    return render(request,'user/register.html')


#注册前的准备
#验证码的准备：
def getcaptcha(request):
    image=ImageCaptcha(fonts=[os.path.abspath('captcha/segoesc.ttf')])
    code=random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    request.session['code']="".join(code)
    data=image.generate("".join(code))
    print(data)
    return HttpResponse(data,'image/png')

#验证邮箱和手机号，不能为空。邮箱注意格式；
def check_email(request):
    rule="\w+@\w+.com"
    val=request.POST.get('vals')

    result = re.findall(rule, val)
    print(result)
    if val=='':
        return HttpResponse('不能为空，谢谢您呢')
    a=TUser.objects.filter(email=val)
    if a:
        return HttpResponse('该邮箱已经被注册')
    if result:
        return HttpResponse('yes')
    else:
        return HttpResponse('邮箱格式错误')

#密码的检验：
def check_pwd(request):
    val=request.POST.get('val')

    if val=='':
        return HttpResponse('0')
    else:
        x,y,z=0,0,0
        for i in val:
            if i.isdigit():
                x+=1
            if i.isalpha():
                y+=1
            else:
                z+=1
        if x==len(val):
            return HttpResponse('1')
        elif x+y==len(val):
            return HttpResponse('2')
        else:
            return HttpResponse('3')
#密码的重复检验：
def re_check_password(request):
    re=request.POST.get('re')
    pwd=request.POST.get('pwd')
    print(re)
    if re==pwd:

        return HttpResponse('yes')
    if re=='':
        return HttpResponse('kong')
    else:
        return HttpResponse('no')
#验证码的校验：
def catecha(request):
    b=request.POST.get('catecha')
    a=request.session.get('code')
    print(a,b)
    if a.casefold()==b.casefold():
        return HttpResponse('ok')
    if b=='':
        return HttpResponse('kong')
    else:
        return HttpResponse('error')
#加密：
def hash_code(a,salt='123'):
    h=hashlib.sha256()
    a+=salt
    h.update(a.encode())
    return h.hexdigest()

#生成邮箱验证：
def confirm(user):
    now=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    code=hash_code(user,now)
    return code

#注册过程：
def send_mail(email, email_getcha):

    subject, from_email, to = '邮箱验证码登陆请求', 'yintiannong@sina.com', email

    text_content = '欢迎访问百知系统，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/user_app/confirm/?code={}" target=blank>www.baidu.com</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1:8000',email_getcha)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def regist(request):
    #收集信息：
    username=request.POST.get('txt_username')
    password=request.POST.get('txt_password')
    pwd=make_password(password)
    email_getcha = confirm(username)
    email=request.POST.get('email')
    send_mail(email,email_getcha)
    TUser.objects.create(email=username,pwd=pwd,email_getcha=email_getcha)
    a=redirect('yh:zccg')
    request.session['username']=username
    return a


def regist_ok(request):
    username=request.session.get('username')
    car2=request.session.get('car2')
    if car2:
        del request.session['car2']
        request.session['username'] = username
        return redirect('dz:dz')
    return render(request,'user/register ok.html',{'username':username})

#登录：

def login_page(request):
    return render(request,'user/login.html')



def login(request):
    username=request.POST.get('txtUsername')

    pwd=request.POST.get('txtPassword')

    c=TUser.objects.filter(email=username)
    print(len(c))
    if c :
        pwd1 = TUser.objects.get(email=username).pwd
        check_password(pwd, pwd1)
        return HttpResponse('yes')
    if len(username)==0:
        return HttpResponse('kong')
    else:
            return HttpResponse('cuo')

def login1(request):
    car2=request.session.get('car2')
    username=request.POST.get('txtUsername')
    request.session['username']=username
    request.session['ok']=1
    a = redirect('book_fl:sy')
    if car2:
        del request.session['car2']
        return redirect('dz:dz')
    else:
        return a

def check_emails(request):
    code=request.GET.get('code')
    a=TUser.objects.filter(email_getcha=code)
    if a:
        return render(request,'email.html')
    else:
        return redirect('yh:zc')