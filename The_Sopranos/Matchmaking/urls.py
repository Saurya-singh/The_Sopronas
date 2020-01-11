from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('status_list',views.status_list,name='status_list'),
    path('home',views.home, name='home'),
    path('notification',views.notification, name='nofification'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('search',views.search, name='search'),
]