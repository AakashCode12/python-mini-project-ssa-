
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from django.contrib import messages
from .models import Song, Artist, Category, Language
# import collections


def index(request):
    all_songs = Song.objects.all()
    context = {
        'all_songs': all_songs
    }
    return render(request, 'index.html', context)
