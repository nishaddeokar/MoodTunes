import unittest
from unittest.mock import patch, Mock
from generatePlaylist import generate_playlist 

class TestGeneratePlaylist(unittest.TestCase):
    @patch('generatePlaylist.spotipy.Spotify')  
    def test_generate_playlist(self, MockSpotify):
        # Mocking Spotipy's Spotify class instance
        mock_sp = MockSpotify()
        
        # Fake data
        mock_sp.current_user_top_tracks.return_value = {'items': [{'id': '1'}, {'id': '2'}, {'id': '3'}, {'id': '4'}]}
        mock_sp.recommendations.return_value = {'tracks': [{'id': '5'}, {'id': '6'}, {'id': '7'}, {'id': '8'}, {'id': '9'}, {'id': '10'}]}
        mock_sp.current_user.return_value = {'id': 'user_id'}
        mock_sp.user_playlist_create.return_value = {'id': 'new_playlist_id'}
        
        # Call the function
        username = "nishaddeokar"
        token = "BQCL0F0RaboF44RVPoLQpUNYEZMOa1rVrKx6verlgc_2ReY_zyPl457vid1g"
        genre = "pop"
        bpm = 100
        result = generate_playlist(username, token, genre, bpm)
        
        # Check if the function returns the expected playlist id
        self.assertEqual(result, 'new_playlist_id')

        # Check if the Spotipy methods were called with the expected arguments
        mock_sp.current_user_top_tracks.assert_called_with(limit=4, time_range="short_term")
        mock_sp.recommendations.assert_called_with(seed_tracks=['1', '2', '3', '4'], seed_genres=[genre], limit=10, target_tempo=bpm)
        mock_sp.user_playlist_create.assert_called_with(user='user_id', name=f"BPM {bpm}", description=unittest.mock.ANY)  # using ANY as the date changes dynamically
        mock_sp.user_playlist_add_tracks.assert_called_with(user='user_id', playlist_id='new_playlist_id', tracks=['5', '6', '7', '8', '9', '10'])

if __name__ == "__main__":
    unittest.main()