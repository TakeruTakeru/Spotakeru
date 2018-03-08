import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'e6447eec6f8448d7a80b1c45a8237034'
client_secret = '98e4103299954b18a51fa991db7d6741'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'rihanna'
result = spotify.search(q='artist:' + name, type='artist')
for i in result['artists']['items']:
    print("{0} popularity: {1}".format(i['name'], i['popularity']))
