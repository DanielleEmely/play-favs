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
