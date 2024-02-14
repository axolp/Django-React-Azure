from django.urls import path
from . import views

urlpatterns= [
    path('',views.home ),
    path('fiszki', views.fiszki, name="fiszki"),
]