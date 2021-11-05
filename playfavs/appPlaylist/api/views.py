from django.shortcuts import render
from django.http import JsonResponse

from ..models import Playlist, Musica, Artista

from .serializers import PlaylistSerializer, MusicaSerializer, ArtistaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List-Create Playlist': '/playlist-list-create/',
        'Detail-Update-Delete Playlist': '/playlist-detail-update-delete/<str:pk>/',
        'List-Create Artista': '/artistas-list-create/',
        'Detail-Update-Delete Artista': '/artistas-detail-update-delete/<str:pk>/',
        'List-Create Musica': '/musicas-list-create/',
        'Detail-Update-Delete Musica': '/musicas-detail-update-delete/<str:pk>/',
		}

	return Response(api_urls)

# CRUD api das playlists

# Funções para as requisições de arcordo com o tipo
# As requisições foram separadas de acordo com a obrigatoriedade de argumentos
# Cada model possui sua view de requisição GET (com e sem arguemento) POST PUT e DELETE

@api_view(['GET', 'POST'])
def playlist_list_create(request):
    if request.method == 'GET':
        plays = Playlist.objects.all().order_by('-id')
        serializer = PlaylistSerializer(plays, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def playlist_get_put_delete(request, pk):
    if request.method == 'GET':
        playlists = Playlist.objects.get(id=pk)
        serializer = PlaylistSerializer(playlists, many=False)
        return Response(serializer.data)
    elif request == 'PUT':
        play = Playlist.objets.get(id=pk)
        serializer = PlaylistSerializer(play, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request == 'DELETE':
        play = Playlist.objects.get(id=pk)
        play.delete()
        return Response('Playlist apagada sucesso!')


# CRUD api dos artistas
@api_view(['GET', 'POST'])
def artista_list_create(request):
    if request.method == 'GET':
        artistas = Artista.objects.all().order_by('-id')
        serializer = ArtistaSerializer(artistas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def artista_get_put_delete(request, pk):
    if request.method == 'GET':
        artista = Artista.objects.get(id=pk)
        serializer = ArtistaSerializer(artista, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        artista = Artista.objets.get(id=pk)
        serializer = ArtistaSerializer(artista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        artista = Artista.objects.get(id=pk)
        artista.delete()
        return Response('Artista apagadp com sucesso!')

# CRUD api das musicas

@api_view(['GET', 'POST'])
def musicas_list_create(request):
    if request.method == 'GET':
        musicas = Musica.objects.all().order_by('-id')
        serializer = MusicaSerializer(musicas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def musica_get_put_delete(request, pk):
    if request.method == 'GET':
        musica = Musica.objects.get(id=pk)
        serializer = MusicaSerializer(musica, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        musica = Musica.objets.get(id=pk)
        serializer = MusicaSerializer(musica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        musica = Musica.objects.get(id=pk)
        musica.delete()
        return Response('Musica apagada com sucesso!')