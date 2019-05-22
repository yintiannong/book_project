from django.urls import path


import user_app.views
from user_app import views

urlpatterns = [
   path('regist_page/',views.regist_page,name='zc'),
   path('captcha/',views.getcaptcha,name='yzm'),
   path('check_email/',views.check_email,name='jcem'),
   path('check_password/',views.check_pwd,name='jcma'),
   path('re_check_pwd/',views.re_check_password,name='re_pwd'),
   path('check_catecha/',views.catecha,name='check_yzm'),
   path('regist/',views.regist,name='regist'),
   path('login_page/',views.login_page,name='dljm'),
   path('login/',views.login,name='dl'),
   path('logn1/',views.login1,name='dl1'),
   path('redist_ok/',views.regist_ok,name='zccg'),
   path('confirm/',views.check_emails,name='yx')

]
