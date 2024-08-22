# Importing the API and instantiating the client using my keys
from terra.base_client import Terra
import webbrowser

def set(ref_id):

    terra = Terra(API_KEY, DEV_ID, SECRET)

    widget_response = terra.generate_widget_session(
        reference_id=ref_id,
        providers=["GOOGLE"],
        auth_success_redirect_url="http://127.0.0.1:3000/auth",
        auth_failure_redirect_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        language="en").get_parsed_response()

    webbrowser.open_new_tab(widget_response.url)
