from django.urls import path
from .views import *

urlpatterns = [
    path('customersignup/', CustomerSignup.as_view(), name='customersignup'),
    path('adminsignup/', AdminSignup.as_view(), name='signup'),
    path('salessignup/', SalesSignup.as_view(), name='signup'),

    # path('login/', Login.as_view(), name='login'),
    path('test/view/', TestView.as_view(), name='test_view'),
    path('logout/', Logout.as_view(), name='logout')
]