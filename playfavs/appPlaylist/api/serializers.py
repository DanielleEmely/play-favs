from rest_framework import serializers
from playfavs.appPlaylist.models import Playlist, Artista, Musica

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'