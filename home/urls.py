from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kanpur', views.kanpur, name='kanpurfare'),
    path('result', views.result, name='result'),
    path('timings', views.timings, name='timings'),
    path('kochi_fare', views.kochifare, name='kochifare'),
    path('kochi_result', views.kochiresult, name='kochiresult'),
    path('jaipur_fare', views.jaipurfare, name='jaipurfare'),
    path('jaipur_result', views.jaipurresult, name='jaipurresult'),
    path('nagpur', views.nagpurfare, name='nagpurfare'),
    path('nagpur_result', views.nagpurresult, name='nagpurresult'),
    path('add', views.add, name='add'),
    path('adding', views.adding, name='adding'),
    path('chennai_fare',views.chennaifare, name='chennaifare'),
    path('chennai_result', views.chennairesult, name='chennairesult'),
    path('hyderabad_fare',views.hyderabadfare, name='hyderabadfare'),
    path('hyderabad_result',views.hyderabadresult, name='hyderabadresult')
    


]