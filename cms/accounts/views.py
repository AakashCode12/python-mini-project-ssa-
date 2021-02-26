
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Song, Artist, Album, Language
import math


def index(request):
    all_trending_songs = Song.objects.filter(trending=True)
    top_three = []
    if len(all_trending_songs) >= 3:
        for i in range(3):
            top_three.append(all_trending_songs[i])
    else:
        for i in range(len(all_trending_songs)):
            top_three.append(all_trending_songs[i])

    front_page_artists = Artist.objects.filter(front_page=True)

    context = {
        'all_songs': all_trending_songs,
        'top_three_songs': top_three,
        'front_page_artists': front_page_artists,
    }
    return render(request, 'index.html', context)


def albums(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'album.html', context)


def artists(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(request, 'artist.html', context)


def artist1(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'artist_profile.html', context)


def allsongs(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'all_songs.html', context)


def openAlbum(request, albumid):
    # album = Album.objects.filter(pk=albumid)
    songs = Song.objects.filter(album__pk=albumid)
    context = {
        'songs': songs,
        'song1': songs[0],
    }
    return render(request, 'albumsongs.html', context)


def songsPlay(request, myid):
    song = Song.objects.filter(pk=myid)
    return render(request, 'play_song.html', {'song': song[0]})


def openArtist(request, artistid):
    # songs = Song.objects.filter(artist__pk=artistid)
    # context = {
    #     'songs': songs,
    # }
    artist = Artist.objects.filter(pk=artistid)
    albums = Album.objects.filter(artist=artist)

    context = {
        'artist': artist,
        'album': albums,
    }
    return render(request, 'artist_profile.html', context)


def searchSong(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        all_songs_name = Song.objects.filter(
            name__icontains=query)
        context = {
            'all_songs_name': all_songs_name,
            'query': query,
            'search_mode_on': True
        }
        return render(request, "search_result.html", context)
    else:
        context = {'search_mode_on': False}
    return render(request, "search_result.html", context)
