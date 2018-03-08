import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = 'e6447eec6f8448d7a80b1c45a8237034'
client_secret = '98e4103299954b18a51fa991db7d6741'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

lz_url = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
results = spotify.artist_top_tracks(lz_url)

for track in results['tracks'][:10]:
    print("track : " + track["name"])
    print("audio : " + track["preview_url"])
    print("cover art : " + track["album"]["images"][0]["url"])
