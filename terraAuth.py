# Importing the API and instantiating the client using my keys
from terra.base_client import Terra
import webbrowser

def set(ref_id):
    API_KEY = "020f5b152d76c975fd256ea2a81b520938b274dc73413b45fa231baee64a1018"
    DEV_ID = "impeatrial-dev-R4tRG6iTLV"
    SECRET = "bef95ca4ced3d6b9fb114baa3aa85d0be022818668fa3ea7"

    terra = Terra(API_KEY, DEV_ID, SECRET)

    widget_response = terra.generate_widget_session(
        reference_id=ref_id,
        providers=["GOOGLE"],
        auth_success_redirect_url="http://127.0.0.1:3000/auth",
        auth_failure_redirect_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        language="en").get_parsed_response()

    webbrowser.open_new_tab(widget_response.url)
