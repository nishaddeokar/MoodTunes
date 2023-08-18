# Datetime objects required as input to some API calls
from datetime import datetime
from terra.base_client import Terra

def get_json():
    API_KEY = "020f5b152d76c975fd256ea2a81b520938b274dc73413b45fa231baee64a1018"
    DEV_ID = "impeatrial-dev-R4tRG6iTLV"
    SECRET = "bef95ca4ced3d6b9fb114baa3aa85d0be022818668fa3ea7"

    terra = Terra(API_KEY, DEV_ID, SECRET)

    # terra.deauthenticate_user(terra.list_users().get_parsed_response().users[0])
    # parsed_api_response = terra.list_users().get_parsed_response().users
    # print(parsed_api_response)

    # Create a user object
    # USER_ID = "9b0c57f7-8549-461e-b003-d58a7c573ee2"
    # terra_user = terra.from_user_id(USER_ID)

    # # Get the nutrition data from start date to current time
    # sleep_resp = terra_user.get_activity(start_date=datetime.strptime('2023-08-09','%Y-%m-%d'), end_date=datetime.now(), to_webhook = False )
    # sleep_resp_json = sleep_resp.get_json()
    # return sleep_resp_json

get_json()