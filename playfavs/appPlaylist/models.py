from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Artista(models.Model):
    nome_do_artista = models.CharField(max_length=200)
    def __str__(self):
        return self.nome_do_artista

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    #toda musica está vinculada a um artista (com restrição de integridade referencial de exluscao)
    artista_da_musica = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Playlist(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_playlist = models.CharField(max_length=200)
    # na playlist, com o ForeignKey de model, temos um relacionmaneto (1:n), onde há um referência para musica
    # portanto, caso eu queira acessar os dados daquela musica, posso pegá-los pela chave FK
    # com isso, são acessados, titulo e artista, e por consequência do relacionamento da
    # musica com seu artista, pode-se chegar até os dados do artista de uma música também.
    musicas = models.ForeignKey(Musica, on_delete=models.CASCADE, default=1)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_playlist