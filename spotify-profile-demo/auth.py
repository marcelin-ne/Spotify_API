import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Auth:
    client_id = '185dc74bb30649d888e8145596e78d6a'
    client_secret = '68fda681626f48d794287916788bafa1'
    redirect_uri = 'http://localhost:3000/callback'
    scope = 'user-library-read user-read-email user-top-read playlist-read-private'

    @classmethod
    def generate_token(cls):
        sp_oauth = SpotifyOAuth(client_id=cls.client_id,
                                client_secret=cls.client_secret,
                                redirect_uri=cls.redirect_uri,
                                scope=cls.scope)
        token_info = sp_oauth.get_access_token()
        return token_info['access_token']

    @classmethod
    def get_token(cls):
        # Intenta obtener el token almacenado
        token = os.environ.get('SPOTIPY_TOKEN')
        if token:
            return token

        # Si no hay token almacenado o ha caducado, genera uno nuevo
        token = cls.generate_token()
        # Almacena el token para su uso posterior
        os.environ['SPOTIPY_TOKEN'] = token
        return token