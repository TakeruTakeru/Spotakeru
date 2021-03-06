import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import os




class Spotakeru(spotipy.Spotify):

    def security(self):

        client_id = os.environ["SPOTIFY_ID"]
        client_secret = os.environ["SPOTIFY_SECRET"]

        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return spotify

    def search(self, name):

        spotify = self.security()
        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=10, type='artist')
        return result
