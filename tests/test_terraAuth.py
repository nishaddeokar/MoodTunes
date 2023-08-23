import unittest
from unittest.mock import patch, Mock
from terraAuth import set  # The function you're going to test

class TestTerraAuth(unittest.TestCase):

    @patch('terraAuth.Terra')
    @patch('terraAuth.webbrowser.open_new_tab')
    def test_set_function(self, mock_open_new_tab, mock_terra):
        # Mocking generate_widget_session
        mock_terra_instance = mock_terra.return_value
        mock_generate_widget_response = Mock()
        mock_generate_widget_response.get_parsed_response.return_value = {'url': 'mock_url'}
        mock_terra_instance.generate_widget_session.return_value = mock_generate_widget_response

        # Calling the function to test
        set("some_ref_id")

        # Verifying the Terra class is initialized with correct values
        mock_terra.assert_called_with("020f5b152d76c97dc73413b45fa231baee64a1018", "impeatrial-dev-R4t", "bef95ca4ced3d6b9fb114baa3aa85d0")

        # Verifying generate_widget_session is called with correct parameters
        mock_terra_instance.generate_widget_session.assert_called_with(
            reference_id="some_ref_id",
            providers=["GOOGLE"],
            auth_success_redirect_url="http://127.0.0.1:3000/auth",
            auth_failure_redirect_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            language="en"
        )

        # Verifying webbrowser.open_new_tab is called with correct url
        mock_open_new_tab.assert_called_with('mock_url')

if __name__ == '__main__':
    unittest.main()
