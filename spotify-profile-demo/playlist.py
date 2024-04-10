import spotipy
import requests 
import re

class Playlist:
    
    def get_playlist_id_from_url(self, url):
        # Esta expresión regular busca patrones que coincidan con los IDs de las playlists de Spotify
        pattern = r"spotify:playlist:(\w+)|https://open.spotify.com/playlist/(\w+)"
        match = re.search(pattern, url)
        if match:
            # Retorna el primer grupo que no sea None
            return match.group(1) or match.group(2)
        else:
            raise ValueError("URL inválida. Asegúrate de que sea una URL de playlist de Spotify.")
    
    def save_playlist_cover(self, file_path, playlist_id, sp):
        playlist_info = sp.playlist(playlist_id)
        cover_url = playlist_info['images'][0]['url']
        response = requests.get(cover_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"La portada de la playlist ha sido guardada en {file_path}")
        else:
            print("No se pudo descargar la portada de la playlist.")

    def get_followers_count(self, playlist_id, sp):
        playlist_info = sp.playlist(playlist_id)
        followers_count = playlist_info['followers']['total']
        return followers_count

    def get_average_audio_features(self, playlist_id, sp):
        playlist_tracks = sp.playlist_tracks(playlist_id)['items']
        num_tracks = len(playlist_tracks)

        # Inicializar el diccionario para almacenar las sumas de características de audio
        total_audio_features = {
            'Tempo(BPM)': 0,
            'Acousticness': 0,
            'Danceability': 0,
            'Energy': 0,
            'Instrumentalness': 0,
            'Liveness': 0,
            'Loudness': 0,
            'Valence': 0
        }

        # Sumar características de audio de todas las pistas en la lista de reproducción
        for track in playlist_tracks:
            audio_features = sp.audio_features(track['track']['id'])[0]
            if audio_features:  # Verificar si se obtuvieron características de audio para la pista
                total_audio_features['Tempo(BPM)'] += audio_features.get('tempo', 0)
                total_audio_features['Acousticness'] += audio_features.get('acousticness', 0)
                total_audio_features['Danceability'] += audio_features.get('danceability', 0)
                total_audio_features['Energy'] += audio_features.get('energy', 0)
                total_audio_features['Instrumentalness'] += audio_features.get('instrumentalness', 0)
                total_audio_features['Liveness'] += audio_features.get('liveness', 0)
                total_audio_features['Loudness'] += audio_features.get('loudness', 0)
                total_audio_features['Valence'] += audio_features.get('valence', 0)

        # Calcular promedio de características de audio
        average_audio_features = {
            feature: total / num_tracks if num_tracks != 0 else 0 for feature, total in total_audio_features.items()
        }
        return average_audio_features

    def get_avarage_cover_features(self, playlist_id, cover_path, sp):
        # Guardar la portada de la playlist
        self.save_playlist_cover(cover_path, playlist_id, sp)

        # Obtener el valor medio de los parámetros de audio
        average_audio_features = self.get_average_audio_features(playlist_id, sp)
        print("Valor medio de los parámetros de audio:")
        for feature, value in average_audio_features.items():
            print(f"{feature}: {value}")

        # Obtener el número de seguidores de la playlist
        followers_count = self.get_followers_count(playlist_id, sp)
        print(f"Número de seguidores de la playlist: {followers_count}")

        return average_audio_features, followers_count
