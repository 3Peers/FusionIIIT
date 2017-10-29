from django.conf.urls import url

from . import views

app_name = 'visitorhostel'

urlpatterns = [

    url(r'^$', views.visitorhostel, name='visitorhostel'),
    url(r'^vh_homepage/', views.vh_homepage, name ='vh_homepage'),
    url(r'^vh_booking_request/' , views.booking_request , name ='booking_request'),
    url(r'^view_booking/', views.all_booking, name = 'view_all_booking'),
    url(r'^cancel_booking/', views.cancel_booked_booking, name = 'cancel_booking'),
    url(r'^checkin/', views.check_in, name = 'cancel_booking'),
]
