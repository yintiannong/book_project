from django.urls import path

from shopping_car_app import views

urlpatterns = [
    path('shopping_car_page/',views.shopp_car_page,name='gwc_page'),
    path('add_car/',views.add,name='tj_goods'),
    path('change/',views.change,name='gb_goods'),
    path('del_goods/',views.del_goods,name='sc_goods'),
    path('settlment/',views.settlement,name='js'),
    path('huifu/',views.huifu_goods,name='hf')


]
