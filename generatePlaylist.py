import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from datetime import datetime

def generate_playlist(username, token, genre, bpm):
    sp = spotipy.Spotify(auth=token)
    top = sp.current_user_top_tracks(limit=4, time_range="short_term")
    top_track_ids = []
    for item in top['items']:
        top_track_ids.append(item['id'])
    r = sp.recommendations(seed_tracks=top_track_ids, seed_genres=[genre], limit=10, target_tempo=bpm)
    rec_track_ids = []
    for item in r['tracks']:
        rec_track_ids.append(item['id'])
    new_playlist = sp.user_playlist_create(user=sp.current_user()['id'], name="BPM " + str(bpm), description=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=new_playlist['id'], tracks=rec_track_ids)
    return new_playlist['id']