from django.urls import path
from .views import *

urlpatterns=[
    path('status/',view_get_post_status),
    path('status/<int:ID>',view_getByID_updateByID_deleteByID),
    path('status/<int:pageNo>/<int:items>',pagination)
]