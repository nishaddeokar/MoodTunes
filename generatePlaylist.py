import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from datetime import datetime

def generate_playlist(username, token, genre, bpm):
    try:
        token = util.prompt_for_user_token(username, client_id="bc9d7e2bdf84441fb295477c2fe03c33",
                                                     client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
                                                     redirect_uri="http://127.0.0.1:5000/", 
                                                     scope = "user-top-read playlist-modify-public")
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, client_id="bc9d7e2bdf84441fb295477c2fe03c33",
                                                     client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
                                                     redirect_uri="http://127.0.0.1:5000/", 
                                                     scope = "user-top-read playlist-modify-public")
    sp = spotipy.Spotify(auth=token)
    top = sp.current_user_top_tracks(limit=4, time_range="short_term")
    top_track_ids = []
    for item in top['items']:
        top_track_ids.append(item['id'])
        print(item['name'])
    r = sp.recommendations(seed_tracks=top_track_ids, seed_genres=[genre], limit=10, target_tempo=bpm)
    rec_track_ids = []
    for item in r['tracks']:
        rec_track_ids.append(item['id'])
    new_playlist = sp.user_playlist_create(user=sp.current_user()['id'], name="BPM " + str(bpm), description=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=new_playlist['id'], tracks=rec_track_ids)
    return new_playlist['id']

# auth_manager=SpotifyOAuth(client_id="bc9d7e2bdf84441fb295477c2fe03c33",
#                                                 client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
#                                                 redirect_uri="http://127.0.0.1:5000/", 
#                                                 scope = "user-top-read playlist-modify-public")
