import requests
from bs4 import BeautifulSoup
import json
from private import client_id, client_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_to_travel = input("Which year do you want to travel to? "
                       "Type the datein this format YYYY-MM-DD: ")

billboard_endpoint = "https://www.billboard.com/charts/hot-100/"

URL = billboard_endpoint+date_to_travel

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_tags = soup.findAll(class_="chart-element__information__song")
artist_tags = soup.findAll(class_="chart-element__information__artist")


song_details = {song_tag.getText(): artist_tag.getText() for song_tag, artist_tag in zip(song_tags, artist_tags)}




with open("dump.json", "w") as file:
    json.dump(song_details,file ,indent=4)


redirect = "http://example.com"
scope = "playlist-modify-private"

auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect,
    scope=scope,
    show_dialog=True,
    cache_path="token.txt"
)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
# print(user_id)


song_uris = []
year = date_to_travel.split("-")[0]
for song_name,artist in song_details.items():
    result = sp.search(q=f"track:{song_name} year:{year} artist: {artist}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")
        
# song = "Believer - imagine dragons"

playlist_name = "Billboard 100 "+date_to_travel
playlist = sp.user_playlist_create(user=user_id,name=playlist_name,public=False,description="Just learning some stuff")

# print(playlist)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"],tracks=song_uris)
