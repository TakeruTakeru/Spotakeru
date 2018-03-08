import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint
import json

client_id = 'e6447eec6f8448d7a80b1c45a8237034'
client_secret = '98e4103299954b18a51fa991db7d6741'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'RIRI'

result = spotify.search(q="artist:" + search_str, limit=10, type='artist')
for i in result['artists']['items']:
    print("{0} URL→ {1}".format(i["name"], i['external_urls']))

print("artist{}".format(result))

class Spotakeru(spotipy.Spotify):

    def search(name):

        client_id = 'e6447eec6f8448d7a80b1c45a8237034'
        client_secret = '98e4103299954b18a51fa991db7d6741'
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=10, type='artist')
        return result
