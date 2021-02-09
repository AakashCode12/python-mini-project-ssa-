
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Song, Artist, Category, Language


def index(request):
    all_songs = Song.objects.all()
    context = {
        'all_songs': all_songs
    }
    return render(request, 'index.html', context)
