## PROJETO DESAFIO WENI :pager:

#### Autora: Danielle Emely de Souza Almeida :wave:

*Contato* danielle.emely.sa@gmail.com

###### Projeto criado para facilitar a organização de músicas, playlists e artistas favoritos. Portanto, foi criada a API PlayFavs, que fornece a possibilidade de usar uma interface que fornece a possibilidade de criar, editar, listar e apagar artistas, músicas e playlists. Para ter acesso aos dados, você deve fazer requisições Rest, usando a API PlayFavs.

###### Para rodar a aplicação, deve-se seguir os seguintes passos descritos em https://www.django-rest-framework.org/#requirements: 

```
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework
```

#### Classes 

As seguintes classes são models, ou seja, herdam as definições das classes Model do Django, para a manipulação de dados em banco de dados. As classes podem ser entendidas como tabelas no banco e seus atributos serão representados como campos da tabela. 

~~~python
class Artista(models.Model)
class Musica(models.Model)
class Playlist(models.Model)
~~~



Para realizar a requisição dos dados por meio de uma API, eles precisam ser serializados. Abaixo seguem as classes usadas para a serialização dos dados de cada model. Essas classes herdam  de ModelSerializer, que foram importadas usando os recursos de Django Rest  Framework.

~~~python
class ArtistaSerializer(serializers.ModelSerializer)
class MusicaSerializer(serializers.ModelSerializer)
class PlaylistSerializer(serializers.ModelSerializer)
~~~

#### Funções

As funções implementadas para as requisições API seguem uma lógica para cada tipo de requisição. As funções foram separadas de acordo com a obrigatoriedade de argumentos de cada requisição, para cada model implementado. As funções que serão apresentadas foram feitas para a view de uma requisição api rest. Tipos de views de requisição:

- GET (com e sem arguemento) ;

- POST;

- PUT;

- DELETE.

  ~~~~python
  # CRUD api das playlists
  
  @api_view(['GET', 'POST'])
  def playlist_list_create(request)
  # O código desta função faz a requisição por meio do verbo GET ou POST e retorna os dados das playlists de acordo com a requisição passada.
  
  @api_view(['GET', 'PUT', 'DELETE'])
  def playlist_get_put_delete(request, pk)
  # O código desta função faz a requisição por meio do verbo GET PUT ou DELETE e retorna os resultados da aplicação do argumento pk e o verbo passados em cima dos dados de uma playlist.
  
  # CRUD api dos artistas
  
  @api_view(['GET', 'POST'])
  def artista_list_create(request)
  # O código desta função faz a requisição por meio do verbo GET ou POST e retorna os dados das artistas de acordo com a requisição passada.
  
  @api_view(['GET', 'PUT', 'DELETE'])
  def artista_get_put_delete(request, pk)
  # O código desta função faz a requisição por meio do verbo GET PUT ou DELETE e retorna os resultados da aplicação do argumento pk e o verbo passados em cima dos dados de um artista.
     
  # CRUD api das musicas
  
  @api_view(['GET', 'POST'])
  def musicas_list_create(request)
  # O código desta função faz a requisição por meio do verbo GET ou POST e retorna os dados das musicas de acordo com a requisição passada.
  
  @api_view(['GET', 'PUT', 'DELETE'])
  def musica_get_put_delete(request, pk)
  # O código desta função faz a requisição por meio do verbo GET PUT ou DELETE e retorna os resultados da aplicação do argumento pk e o verbo passados em cima dos dados de um artista.
  
  ~~~~

  

### *Como usar a API PlayFavs*

Para usar a API e integrar na sua aplicação, você pode acessar como a maioria das APIs, por meio de requisições RestFull. O conteúdo a ser enviado, é um JSON (JavaScript Object Notation). Vejamos alguns exemplos de requisições que você pode fazer. Considerando um servidor localhost de porta 8000.

#### Requisições GET 

- **Exemplos de requisições GET de Playlists**

  Link:

  ```less
  http://127.0.0.1:8000/appPlaylist/playlist-list-create/
  ```

  Corpo da Resposta

  ~~~json
  [
    {
      "id": 3,
      "nome_playlist": "Melhores dos Anos 80",
      "criado": "2021-11-05T01:38:12.302350Z",
      "atualizado": "2021-11-05T01:38:12.302350Z",
      "autor": 1
    },
    {
      "id": 2,
      "nome_playlist": "Minhas Favs",
      "criado": "2021-11-04T16:44:14.908411Z",
      "atualizado": "2021-11-04T16:44:14.908411Z",
      "autor": 1
    }
  ]
  ~~~

  

- **Exemplos de requisições GET de Músicas**

  Link:

  ```less
  http://127.0.0.1:8000/appPlaylist/playlist-list-create/
  ```

  Corpo da Resposta:

  ```json
  [
      {
          "id": 6,
          "titulo": "wide awake",
          "artista_da_musica": 2,
          "playlist_de_origem": 2
      },
      {
          "id": 5,
          "titulo": "Careless Whisper",
          "artista_da_musica": 5,
          "playlist_de_origem": 3
      },
      {
          "id": 4,
          "titulo": "Billie Jean",
          "artista_da_musica": 4,
          "playlist_de_origem": 3
      },
      {
          "id": 3,
          "titulo": "Bonekinha",
          "artista_da_musica": 1,
          "playlist_de_origem": 2
      }
  ]
  ```

- **Exemplos de requisições GET de Artistas**

  Link:

  ```less
  http://127.0.0.1:8000/appPlaylist/artistas-list-create/
  ```

  Corpo da Resposta:

  ```json
  [
      {
          "id": 5,
          "nome_do_artista": "George Michael"
      },
      {
          "id": 4,
          "nome_do_artista": "Michael Jackson"
      },
      {
          "id": 3,
          "nome_do_artista": "Shawn Mendes"
      },
      {
          "id": 2,
          "nome_do_artista": "Katy Perry"
      },
      {
          "id": 1,
          "nome_do_artista": "Gloria Groove"
      }
  ]
  ```

- **Exemplos de requisições POST**

  Nesta sessão apresentarei dois exemplos de uma requisição post de uma Música,  mostrando um caso de erro na requisição de uma música que não possui id válido para um artista, isso significa que uma música deve estar associada a um artista, assim como deve estar em uma Playlist.

  Link:

  ```less
  http://127.0.0.1:8000/appPlaylist/musicas-list-create/
  ```

  Conteúdo do corpo da requisição:

  ~~~~json
   {
          "id": 3,
          "titulo": "Roar",
          "artista_da_musica": 2,
          "playlist_de_origem": 2
  }
  ~~~~

  Resposta:

  ```json
  Content-Type: application/json
  Vary: Accept
  
  {
      "id": 7,
      "titulo": "Roar",
      "artista_da_musica": 2,
      "playlist_de_origem": 2
  }
  ```

  Conteúdo do corpo de uma requisição:

  ~~~ json
  {
      "id": 7,
      "titulo": "Roar",
      "artista_da_musica": 13,
      "playlist_de_origem": 5
  }
  ~~~

  Resposta com Bad Request, problema na requisição.

  ```json
  HTTP 400 Bad Request
  Allow: OPTIONS, GET, POST
  Content-Type: application/json
  Vary: Accept
  
  {
      "artista_da_musica": [
          "Pk inválido \"13\" - objeto não existe."
      ],
      "playlist_de_origem": [
          "Pk inválido \"5\" - objeto não existe."
      ]
  }
  ```

- **Exemplos de requisições PUT e DELETE** 

  Nesta sessão apresentarei a exclusão de uma musica com o id 3. Passando no link o argumento, que é  id da música que desejo apagar.

  Link:

  ```less
  http://127.0.0.1:8000/appPlaylist/musicas-detail-update-delete/3/
  ```

  Corpo da resposta: 

  ```json
  "Musica apagada com sucesso!"
  ```

