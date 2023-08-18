import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

def get(username):
    try:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, client_id="bc9d7e2bdf84441fb295477c2fe03c33",
                                                                 client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
                                                                 redirect_uri="http://127.0.0.1:5000/", 
                                                                 scope = "user-top-read playlist-modify-public")
    except:
        token = util.prompt_for_user_token(username, client_id="bc9d7e2bdf84441fb295477c2fe03c33",
                                                                client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
                                                                redirect_uri="http://127.0.0.1:5000/", 
                                                                scope = "user-top-read playlist-modify-public")
    return token
    # sp = spotipy.Spotify(auth=token)
    # top = sp.current_user_top_tracks()
    # track_uris = []
    # for item in top['items']:
    #     track_uris.append(item['uri'])
    # return track_uris

# export CLIENT_ID="bc9d7e2bdf84441fb295477c2fe03c33"
# export CLIENT_SECRET="779e3b9132bb4c50ba58bec0e87f3f05"
# export REDIRECT_URI="https://open.spotify.com/"