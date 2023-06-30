import requests
import json
import pandas as pd
import datetime
#from folder import export_csv_to_folder
def load_metadata():
    with open("v2_code\metadata.json") as file:
        metadata = json.load(file)
    return metadata

params = load_metadata()

# Define URL
url = params['graph_domain'] + '/debug_token'

# Define Endpoint Parameters
endpointParams = {
    'input_token': params['access_token'],
    'access_token': params['access_token']
}

def main():
    target = ["country", "city", "gender"]
    url = params['endpoint_base'] + params['instagram_account_id'] + '/insights'
    endpointParams = dict()
    endpointParams['metric'] = 'audience_city,audience_country,audience_gender_age' 
    endpointParams['period'] = 'lifetime' 
    endpointParams['access_token'] = params['access_token']
    get_demographics_data(url, target)

if __name__ == "__main__":
    main()