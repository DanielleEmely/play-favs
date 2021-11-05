from django.urls import path
from . import views

app_name = 'appPlaylist'

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	#Seguem os endereços de links para criar/editar/listar/ler dados dos Models criados
	#Cada um com uma view referente aos tipos de requisições com e sem argumentos

	#playlist
	path('playlist-list-create/', views.playlist_list_create, name="playlist-list-create"),
	path('playlist-detail-update-delete/<str:pk>/', views.playlist_get_put_delete, name="playlist-detail-update-delete"),

	#artistas
	path('artistas-list-create/', views.artista_list_create, name='artistas-list-create'),
	path('artistas-detail-update-delete/<str:pk>/', views.artista_get_put_delete, name='artista-detail-update-delete'),

	#musicas
	path('musicas-list-create/', views.musicas_list_create, name='musicass-list-create'),
	path('musicas-detail-update-delete/<str:pk>/', views.musica_get_put_delete, name='musicas-detail-update-delete'),

]

