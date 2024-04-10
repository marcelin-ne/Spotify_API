from consultor import Consultor
from playlist import Playlist
from auth import Auth
import spotipy
from dataExporter import DataExporter

class Main:
    def menu(self):
        print("1. Consultar los 10 artistas más escuchados.")
        print("2. 5 generos favoritos")
        print("3. 10 canciones mas escuchadas")
        print("4. Obtener el valor medio de los parámetros de audio de la playlist.")
        choice = input("Seleccione una opción: ")
        token = Auth.get_token()
        sp = spotipy.Spotify(auth=token)
        if choice == '1':
            top_artists = Consultor.get_top_artists()
            # Imprimir los 10 artistas más escuchados
            print("Los 10 artistas más escuchados:")
            for i, artist in enumerate(top_artists, start=1):
                print(f"{i}. {artist}")

            print("Deseas guardar los datos en 1.cvs o 2.json?")
            choice2 = input("Seleccione una opción: ")
            if choice2 == '1':
                DataExporter.export_to_csv(top_artists, 'top_artists.csv')
                print("Datos guardados en top_artists.csv")
            elif choice2 == '2':
                DataExporter.export_to_json(top_artists, 'top_artists.json')
                print("Datos guardados en top_artists.json")
        elif choice == '2':
            print("Los 5 generos escuchados:")
            top_genres = Consultor.get_top_genres()
            print("Los 5 géneros más escuchados de los artistas más escuchados:" , top_genres)
            print("Deseas guardar los datos en 1.cvs o 2.json?")
            choice2 = input("Seleccione una opción: ")
            if choice2 == '1':
                DataExporter.export_to_csv(top_genres, 'top_genres.csv')
                print("Datos guardados en top_genres.csv")
            elif choice2 == '2':
                DataExporter.export_to_json(top_genres, 'top_genres.json')
                print("Datos guardados en top_genres.json")
        elif choice == '3':
            print("Las 10 canciones más escuchadas:")
            top_tracks = Consultor.get_top_tracks()
            for i, track in enumerate(top_tracks, start=1):
                print(f"{i}. {track[0]} - {track[1]}")
            print("Deseas guardar los datos en 1.cvs o 2.json?")
            choice2 = input("Seleccione una opción: ")
            if choice2 == '1':
                DataExporter.export_to_csv(top_tracks, 'top_tracks.csv')
                print("Datos guardados en top_tracks.csv")
            elif choice2 == '2':
                DataExporter.export_to_json(top_tracks, 'top_tracks.json')
                print("Datos guardados en top_tracks.json")
        elif choice == '4':
            playlist_url = input("Ingresa el URL de la Playlist:") # ID de la playlist que deseas usar
            playlist = Playlist()
            playlist_id = playlist.get_playlist_id_from_url(playlist_url)
            average_audio_features, followers_count = playlist.get_avarage_cover_features(playlist_id, 'playlist_cover.jpg', sp)
            print(f"Número de seguidores de la playlist: {followers_count}")
            print("Valor medio de los parámetros de audio de la playlist:")
            DataExporter.export_to_json(average_audio_features, 'playlist_audio_features.json')
            for feature, value in average_audio_features.items():
                print(f"{feature}: {value}")
            print("Deseas guardar los datos en 1.cvs o 2.json?")
            choice2 = input("Seleccione una opción: ")
            if choice2 == '1':
                DataExporter.export_to_csv(average_audio_features, 'playlist_audio_features.csv')
                print("Datos guardados en playlist_audio_features.csv")
            elif choice2 == '2':
                DataExporter.export_to_json(average_audio_features, 'playlist_audio_features.json')
                print("Datos guardados en playlist_audio_features.json")

        else:
            print("Opción no válida.")

# Instancia de la clase Main
main = Main()
main.menu()
