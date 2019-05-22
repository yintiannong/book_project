"""baizhi_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categeory_book_app/',include(('categeory_book_app.urls','book_fl'))),
    path('user_app/',include(('user_app.urls','yh'))),
    path('shopping_car_app/',include(('shopping_car_app.urls','gwc'))),
    path('address_list_app/',include(('address_list_app.urls','dz'))),
    path('backstage_app/',include(('backstage_app.urls','ht'))),
]
