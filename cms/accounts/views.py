
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Song, Artist, Category, Language
import math


def index(request):
    all_trending_songs = Song.objects.filter(trending=True)
    song_banner = Song.objects.get(banner=True)
    top_three = []
    for i in range(3):
        top_three.append(all_trending_songs[i])

    front_page_artists = Artist.objects.filter(front_page=True)

    context = {
        'all_songs': all_trending_songs,
        'song_banner': song_banner,
        'top_three_songs': top_three,
        'front_page_artists': front_page_artists,
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


def songsPlay(request, myid):
    song = Song.objects.filter(pk=myid)
    return render(request, 'play_song.html', {'song': song[0]})


def searchSong(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        all_songs_name = Song.objects.filter(
            name__icontains=query)
        context = {
            'all_songs_name': all_songs_name,
            'query': query,
        }
        return render(request, "search_result.html", context)

    return render(request, "search_result.html", context)
