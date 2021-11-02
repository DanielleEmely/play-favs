from django.contrib import admin

# Register your models here.
from .models import Artista, Musica, Playlist

admin.site.register(Artista)
admin.site.register(Musica)
admin.site.register(Playlist)