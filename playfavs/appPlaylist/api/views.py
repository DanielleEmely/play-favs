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
		'List':'/playlist-list/',
		'Detail View':'/playlist-detail/<str:pk>/',
		'Create':'/playlist-create/',
		'Update':'/playlist-update/<str:pk>/',
		'Delete':'/playlist-delete/<str:pk>/',
        'List-Create Artista': '/artistas-list-create/',
        'Detail-Update-Delete Artista': '/artistas-detail-update-delete/<str:pk>/',
        'List-Create Musica': '/musicas-list-create/',
        'Detail-Update-Delete Musica': '/musicas-detail-update-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def playlistList(request):
    plays = Playlist.objects.all().order_by('-id')
    serializer = PlaylistSerializer(plays, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def playlistDetail(request, pk):
	playlists = Playlist.objects.get(id=pk)
	serializer = PlaylistSerializer(playlists, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def playlistCreate(request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def plalistUpdate(request, pk):
    play = Playlist.objets.get(id=pk)
    serializer = PlaylistSerializer(play, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def playlistDelete(request, pk):
    play = Playlist.objects.get(id=pk)
    play.delete()
    return Response('Playlist apagada sucesso!')

# CRUD api dos artistas
@api_view(['GET', 'POST'])
def artista_list_Create(request):
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