from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('',get_login_page, name=''),
    path('home',views.home, name='home'),
    path('notification',views.notification, name='nofification'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('search',views.search, name='search'),
    path('poststatus',views.status_form, name='status_insert'),
    path('<int:id>/',views.status_form,name='status_update'),
    path('list',views.status_list, name="status_list"),
    path('delete/<int:id>/',views.status_delete,name='status_delete'),
    path("login",get_login_page,name="login"),
    path("sign_up",get_sign_up_page,name="sign_up"),
    path("post_create_user",post_create_user),
    path("post_login_user",post_login_user)

]