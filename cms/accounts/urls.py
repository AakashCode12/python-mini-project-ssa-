from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('artists/', views.artists, name="artists"),
    path('albums/', views.albums, name="albums"),
    path('allsongs/', views.allsongs, name="allsongs"),
    path('artist1/', views.artist1, name="artist1"),


    path('songsPlay/<int:myid>/', views.songsPlay, name='songsPlay'),

    # todo form ke path
    path("searchSong", views.searchSong, name='searchSong'),
]
