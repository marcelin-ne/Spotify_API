import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Obtén las credenciales de cliente desde las variables de entorno
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

# Define los ámbitos de autorización que necesitas
scope = 'playlist-read-private user-top-read'

# Crea una instancia de SpotifyOAuth con tus credenciales
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope)

# Obtén el token de acceso
token_info = sp_oauth.get_access_token()

# Crea una instancia de Spotify usando el token de acceso
sp = spotipy.Spotify(auth=token_info['access_token'])

# Ahora puedes usar `sp` para interactuar con la API de Spotify como lo hiciste en tu código
# Por ejemplo:
# Obtener playlists del usuario
print("Mis listas de reproducción:")
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))

# Obtener los mejores artistas del usuario
print("Mis 10 mejores artistas:")
results = sp.current_user_top_artists(time_range='medium_term', limit=10)
for i, item in enumerate(results['items']):
    print(i + 1, item['name'])

# Obtener las mejores pistas del usuario
print("Mis mejores pistas:")
results = sp.current_user_top_tracks(time_range='medium_term', limit=10)
for i, item in enumerate(results['items']):
    print(i + 1, item['name'], '//', item['artists'][0]['name'])
