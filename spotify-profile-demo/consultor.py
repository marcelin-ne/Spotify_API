from auth import Auth
import spotipy

class Consultor:
    # 1. Código para obtener los 10 artistas más escuchados
    @classmethod
    def get_top_artists(cls, time_range='medium_term', limit=10):
        token = Auth.get_token()
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_artists(time_range=time_range, limit=limit)
        top_artists = [artist['name'] for artist in results['items']]
        return top_artists
    #2. Código para obtener los 5 géneros más escuchados de los artistas más escuchados
    @classmethod
    def get_top_genres(cls, time_range='medium_term', limit=10):
        top_artists = cls.get_top_artists(time_range, limit)
        token = Auth.get_token()
        sp = spotipy.Spotify(auth=token)
        genre_counts = {}
        for artist in top_artists:
            artist_info = sp.search(q=f"artist:{artist}", type="artist")
            if artist_info['artists']['items']:
                genres = artist_info['artists']['items'][0]['genres']
                for genre in genres:
                    genre_counts[genre] = genre_counts.get(genre, 0) + 1
        top_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        return top_genres
    #3. 10 Canciones mas escuchadas y sus artistas
    @classmethod
    def get_top_tracks(cls, time_range='medium_term', limit=10):
        token = Auth.get_token()
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        top_tracks = [(track['name'], track['artists'][0]['name']) for track in results['items']]
        return top_tracks
