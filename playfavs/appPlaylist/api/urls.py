from django.urls import path
from . import views

app_name = 'appPlaylist'

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('playlist-list/', views.playlistList, name="playlist-list"),
	path('playlist-detail/<str:pk>/', views.playlistDetail, name="playlist-detail"),
	path('playlist-create/', views.playlistCreate, name="playlist-create"),
	path('playlist-update/<str:pk>/', views.plalistUpdate, name="playlist-update"),
	path('playlist-delete/<str:pk>/', views.playlistDelete, name="-delete"),
	#artistas
	path('artistas-list-create/', views.artista_list_Create, name='artistas-list-create'),
	path('artistas-detail-update-delete/<str:pk>/', views.artista_get_put_delete, name='artista-detail-update-delete'),

	#musicas
	path('musicas-list-create/', views.musicas_list_create, name='musicass-list-create'),
	path('musicas-detail-update-delete/<str:pk>/', views.musica_get_put_delete, name='musicas-detail-update-delete'),

]

