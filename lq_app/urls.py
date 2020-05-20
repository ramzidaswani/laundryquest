from django.conf.urls import url, include
from lq_app import views
from django.urls import path


app_name = 'lq_app'

urlpatterns=[
    path(r'^customer_register/$',views.customer_register,name='c_register'),
    path(r'^customer_login/$',views.user_login,name='c_login'),
    path(r'^customer_dash/$',views.user_login,name='c_dash'),
    path(r'^cusotmer_order/$',views.user_login,name='c_order'),
    path(r'^laundrer_register/$',views.customer_register,name='l_register'),
    path(r'^laundrer_login/$',views.user_login,name='l_login'),
    path(r'^laundrer_dash/$',views.user_login,name='l_dash'),
    path(r'^laundrer_order/$',views.user_login,name='l_order')
]
