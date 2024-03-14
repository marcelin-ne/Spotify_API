import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticación de la aplicación con Spotify
auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

# URI del artista
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

# Recuperar los álbumes del artista
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

# Imprimir el nombre de cada álbum
for album in albums:
    print(album['name'])
