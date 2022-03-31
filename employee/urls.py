from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('home',views.home,name = "Home"),
    path('show/',views.show,name = "show"),
    path('send',views.send,name = "send"),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
]
