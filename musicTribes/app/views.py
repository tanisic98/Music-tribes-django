from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Playlist, Tribe, Song

# Create your views here.
def index(request):
    tribes = Tribe.objects.order_by("created_at")
    context={"tribes":tribes}

    return render(request,"app/index.html",context)

def tribe(request,tribe_id):
    tribe = get_object_or_404(Tribe,pk=tribe_id)
    playlists = Playlist.objects.filter(tribe=tribe)
    context={"tribe":tribe, 
            "playlists":playlists}

    return render(request,"app/tribe.html",context)

def playlist(request,tribe_id,playlist_id):
    tribe = get_object_or_404(Tribe,pk = tribe_id)
    playlist = Playlist.objects.filter(tribe=tribe,pk=playlist_id)
    playlist = playlist[0]
    songs = playlist.songs.all()
    context={"playlist":playlist,
            "songs":songs}

    return render(request,"app/playlist.html",context)
