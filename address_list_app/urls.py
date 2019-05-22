
from django.urls import path, include
from address_list_app import views

urlpatterns = [
    path('address_page/',views.address_page,name='dz'),
    path('check/',views.receiver,name='jc'), #检查邮箱
    path('check_phone/',views.check_phone,name='jcsj'),
    path('submit_order/',views.submit_order,name='tjbd'),
    path('selects/',views.selects,name='choose_address'),
    path('login_out/',views.login_out,name='dc')


]
