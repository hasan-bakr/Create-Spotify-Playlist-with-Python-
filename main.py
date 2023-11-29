import spotipy
from spotipy.oauth2 import SpotifyOAuth
import scraping
from spotipy.oauth2 import SpotifyClientCredentials

#scraping.myTitles

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        show_dialog=True,
        cache_path="token.txt",
        username='YOUR_SPOTIFY_VISIBLE_USERNAME',
    )
)
user_id = sp.current_user()["id"]



song_uris = []
for song_name in scraping.myTitles:
    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        song_uris.append(track_uri)
    else:
        print(f"'{song_name}' not found in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id,name=f"{scraping.date} Billboard 100", public=False)

playlist_description = f'This playlist automatically create with Python for times is {scraping.date}'

sp.playlist_change_details(playlist_id=playlist["id"], description=playlist_description)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Well done!!")
