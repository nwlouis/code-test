from django.contrib import admin
from django.urls import path, re_path
from file_manage import views
from django.conf.urls import url
from django.views.decorators.http import require_POST

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_customer/',views.new_customer,name='new_customer'),
    re_path('customer/(?P<pk>\d+)$', views.customerInfoview.as_view(), name='customer_info'),
    re_path('customer/(?P<pk>\d+)/edit/$', views.customerEditview.as_view(), name='edit_customer'),
    re_path('customer/(?P<pk>\d+)/remove/$', views.customerRemoveview.as_view(), name='remove_customer'),

]