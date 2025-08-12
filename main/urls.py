from django.urls import path
from .views import *

urlpatterns=[
    path('',homepage,name="home"),
    path('delete/<str:id>/',delete,name="delete"),
]


