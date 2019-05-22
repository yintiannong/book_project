from django.urls import path

from categeory_book_app.views import home_page, book, book_list_page

urlpatterns = [
    path('page_home/',home_page,name='sy'),
    path('page_book/',book,name='shu'),
    path('book_list_page/',book_list_page,name='book_list'),


]
