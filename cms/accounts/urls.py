from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('artists/', views.artists, name="artists"),
    path('albums/', views.albums, name="albums"),
    path('allsongs/', views.allsongs, name="allsongs"),

]
