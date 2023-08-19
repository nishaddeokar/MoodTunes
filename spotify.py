import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="bc9d7e2bdf84441fb295477c2fe03c33",
                                               client_secret="779e3b9132bb4c50ba58bec0e87f3f05", 
                                               redirect_uri="https://open.spotify.com/", 
                                               scope = "user-top-read playlist-modify-public"))

top = sp.current_user_top_tracks()
track_uris = []
for item in top['items']:
    if 'track' in item:
        track_uris.append(item['track']['uri'])
test = sp.recommendations(seed_tracks=track_uris,seed_genres=[genre], limit=10,target_tempo=120)

for item in test['tracks']:
    print(item['name'])


# print(top)
# results = sp.current_user_saved_tracks()
# print(idx, item['artists'][0]['name'], " – ", item['name'])
#     {'tracks': [{'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6gZq1Q6bdOxsUPUG1TaFbF'}, 'href': 'https://api.spotify.com/v1/artists/6gZq1Q6bdOxsUPUG1TaFbF', 'id': '6gZq1Q6bdOxsUPUG1TaFbF', 'name': 'Godsmack', 'type': 'artist', 'uri': 'spotify:artist:6gZq1Q6bdOxsUPUG1TaFbF'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
# 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT',
# 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT',
# 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/1w7vC8hjYXhK1fS5cM2fUM'}, 'href': 'https://api.spotify.com/v1/albums/1w7vC8hjYXhK1fS5cM2fUM', 'id': '1w7vC8hjYXhK1fS5cM2fUM', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27382a891641608e2f2d6c3a8b8', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0282a891641608e2f2d6c3a8b8', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485182a891641608e2f2d6c3a8b8', 'width': 64}], 'name': 'Godsmack', 'release_date': '1998-01-01', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:1w7vC8hjYXhK1fS5cM2fUM'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6gZq1Q6bdOxsUPUG1TaFbF'}, 'href': 'https://api.spotify.com/v1/artists/6gZq1Q6bdOxsUPUG1TaFbF', 'id': '6gZq1Q6bdOxsUPUG1TaFbF', 'name': 'Godsmack', 'type': 'artist', 'uri': 'spotify:artist:6gZq1Q6bdOxsUPUG1TaFbF'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN',
# 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'KZ', 'MD', 'UA', 'AL',
# 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL',
# 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 282653, 'explicit': False, 'external_ids': {'isrc': 'USUR19980188'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/5uGsG0LfotfWDq6hql4h53'}, 'href': 'https://api.spotify.com/v1/tracks/5uGsG0LfotfWDq6hql4h53', 'id': '5uGsG0LfotfWDq6hql4h53', 'is_local': False, 'name': 'Voodoo', 'popularity': 66, 'preview_url': None, 'track_number': 12, 'type': 'track', 'uri': 'spotify:track:5uGsG0LfotfWDq6hql4h53'}], 'seeds': [{'initialPoolSize': 995, 'afterFilteringSize': 995, 'afterRelinkingSize': 995, 'id': 'rock', 'type': 'GENRE', 'href':
# None}]}