from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('notification.html',views.notification, name='nofification'),
    path('about.html',views.about, name='about'),
    path('contact.html',views.contact, name='contact'),
    path('search.html',views.search, name='search'),
]