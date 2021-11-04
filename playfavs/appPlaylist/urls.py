from django.urls import path
from . import views

app_name = 'appPlaylist'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:playlist_id>/artista/', views.artista, name='artista'),
    path('<int:playlist_id>/musica/', views.musica, name='musica'),
    #path('playlist/', views.playlist, name='playlist')

]
""""""

"""path('getPlaylist', viewsets.playlists, name='listagem'),
    path('postPlaylist/', viewsets.playlistsPost, name='envio'),
    path('putPlaylist/<str:pk>/', viewsets.plalistPut, name='atualizar'),
    path('deletePlaylist/<str:pk>', viewsets.playlistDel, name='deletar')"""