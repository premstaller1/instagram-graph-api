import requests
import json
import pandas as pd
import datetime

def load_metadata():
    with open("v2_code\metadata.json") as file:
        metadata = json.load(file)
    return metadata

params = load_metadata()

def get_data(url, endpointParams):
    try:
        response = requests.get(url, endpointParams)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

# Define URL
params = load_metadata()
url = params['graph_domain'] + '/debug_token'

# Define Endpoint Parameters
endpointParams = {
    'input_token': params['access_token'],
    'access_token': params['access_token']
}

# Call the get_data() function
data = get_data(url, endpointParams)

# Print the data or perform any other desired operations with it
print(data)