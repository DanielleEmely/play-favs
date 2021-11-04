from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Playlist, Artista, Musica
from django.shortcuts import render, get_object_or_404

def index(request):
    playlists = Playlist.objects.order_by('-criado')[:5]
    conteudo = {'playlists': playlists}
    return render(request, 'appPlaylist/playlist.html', conteudo)

"""def playlist(request):
    playlists = Playlist.objects.order_by('-criado')[:5]
    conteudo = {'playlists': playlists}
    return render(request, 'appPlaylist/playlist.html')"""

def artista(request, musica_id):
    musicas = Musica.objects.filter(id=musica_id)
    conteudo = {'playlist': musicas}
    return render(request, 'appPlaylist/artista.html', conteudo)

def musica(request, playlist_id):
    playlist = Playlist.objects.filter(id=playlist_id)
    conteudo = {'playlist': playlist}
    return render(request, 'appPlaylist/musica.html', conteudo)