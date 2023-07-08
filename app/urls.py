from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ins', views.insertarData, name='insert'),
    path('del/<>/<int:id>/', views.deleteData, name='delete'),
    path('upd/<int:id>/', views.updateData, name='update'),
]
