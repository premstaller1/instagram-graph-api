#set up python environment to retrieve data from API

import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time

params = dict()
params['access_token'] = 'EAAG24jaJaYIBAIyw6jxPH2b3fQDmzRoG2qCOf298WUYl5uMS3SW3SNV0FdvXorVofID8UZAJfCHan5adnPwZCbGdZCSSKVS0HhA3FPPI0mvyRMDZAXvUIZArR3VSZCpBtTjsdR88qYmMbD5ZAk1flNj473VMl53Aieg2IZC0XUAgLsZBkqoiMVUZCi'        # not an actual access token
params['client_id'] = '482557670549890'                  
params['client_secret'] = 'd62937e7f31973871d86b8242430b73e'     
params['graph_domain'] = 'https://graph.facebook.com'
params['graph_version'] = 'v16.0'
params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
params['page_id'] = '482557670549890'                  
params['instagram_account_id'] = '17841447229527043'
params['ig_username'] = 'productminimal'

# Define Endpoint Parameters
endpointParams = dict()
endpointParams['input_token'] = params['access_token']
endpointParams['access_token'] = params['access_token']

# Define URL
url = params['graph_domain'] + '/debug_token'

#create a method to retrieve data from API
def get_data(url, endpointParams):
    #get data from API
    data = requests.get(url, endpointParams)
    access_token_data = json.loads(data.content)
    print("Bis hier gehts")
    return access_token_data

#call method to retrieve data from API
df = get_data(url, endpointParams)
print(df)

