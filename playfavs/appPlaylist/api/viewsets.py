from django.shortcuts import  import render
from playfavs.appPlaylist.models import PlayList, Musica, Artista
from .serializers import PlaylistSerializer, MusicaSerializer, ArtistaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status

@api_view(['GET'])
def playlists(request):
    plays = PlayList.objects.all()
    serializer = PlaylistSerializer(plays, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def playlistsPost(request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def plalistPut(request, pk):
    play = PlayList.objets.get(id=pk)
    serializer = PlaylistSerializer(play, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def playlistDel(request, pk):
    play = PlayList.objects.get(id=pk)
    play.delete()
    return Response('Apagado')
