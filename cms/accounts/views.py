
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Song, Artist, Category, Language


def index(request):
    all_songs = Song.objects.all()
    context = {
        'all_songs': all_songs
    }
    return render(request, 'index.html', context)


def artists(request):
    context = {}
    return render(request, 'artist.html', context)


def albums(request):
    context = {}
    return render(request, 'album.html', context)


def allsongs(request):
    context = {}
    return render(request, 'all_songs.html', context)
