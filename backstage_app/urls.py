from django.urls import path
from backstage_app import views


urlpatterns = [
path('backstage/',views.backstage_page,name='htjm'),
path('add_book_page/',views.addbook_page,name='zjs'),
path('book_list',views.book_list_page,name='book_list'),
path('add_parent_page/',views.add_parent_kind_list_page,name='add_parent_page'),
path('add_child_page/',views.add_child_kind_list_page,name='add_child_page'),
path('address_page/',views.address_page,name='dzjm'),
path('order_list/',views.address_order_page,name='bdjm'),
path('book_kind_page/',views.book_kind_page,name='book_kind'),
path('book_add/',views.addbook,name='tj_book'),
path('add_parent/',views.add_parent,name='tj_parent'),
path('add_child/',views.add_child,name='tj_child'),
path('order_page_list/',views.address_order_page,name='dzbd'),
path('dels/',views.dels,name='sc')


]


