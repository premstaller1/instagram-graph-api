#set up python environment to retrieve data from API

import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from datetime import timedelta
import time
from folder import export_csv_to_folder
from db_upload import upload_value_to_bigquery
import time


params = dict()
params['access_token'] = 'EAAG24jaJaYIBAD9D5CVZAs6weFjBYt8mk2iQ2ZCOeYEo4lXpVtCSeLIjZC4P5MZCJQxggwaHCCadPSgzSGCvLWVbcNLno0BpAmXAGjqtiekQ5hOcqDhO5EaprIujUVjWDq1jZAJHRMawlAZCo5tQaCD46ZBjMNjsfbzeLooG0fjUEW0eUXy2SOHzhh9cl4GqXKWG3fXtx4EVwZDZD'        # not an actual access token
params['client_id'] = '482557670549890'                  
params['client_secret'] = 'd62937e7f31973871d86b8242430b73e'     
params['graph_domain'] = 'https://graph.facebook.com'
params['graph_version'] = 'v16.0'
params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
params['page_id'] = '482557670549890'                  
params['instagram_account_id'] = '17841447229527043'
params['ig_username'] = 'productminimal'

# Define URL
url = params['graph_domain'] + '/debug_token'

#I want to retrieve data from Instagram Graph API
url = params['endpoint_base'] + params['instagram_account_id'] + '/insights'

def get_demographics_data(url):
    
    # Get the current time in UTC
    current_time = time.gmtime()

    # Calculate the start of the current day (since)
    since_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday - 1, 0, 0, 0, 0, 0, 0))

    # Calculate the end of the current day (until)
    until_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday - 1, 23, 59, 59, 0, 0, 0))
    
    
    # Define Endpoint Parameters
    endpointParams = dict()
    endpointParams['metric'] = 'impressions,reach,profile_views'
    endpointParams['period'] = 'day'
    endpointParams['metric_type'] = 'total_value'
    endpointParams['since'] = f'{since_time}'
    endpointParams['until'] = f'{until_time}'
    endpointParams['access_token'] = params['access_token'] 
    
    today = date.today() 
    datum_abruf = today - timedelta(days = 1)  
    datum_abruf = datum_abruf.strftime('%Y-%m-%d')
    
    data = requests.get(url, endpointParams)
    access_token_data = json.loads(data.content)
    for item in access_token_data['data']:
        category = item['name']
        value = item['total_value']['value']
        print(f"{category}: {value}")
        upload_value_to_bigquery(value, category, datum_abruf)
get_demographics_data(url)