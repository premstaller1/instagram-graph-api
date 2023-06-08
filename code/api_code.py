#set up python environment to retrieve data from API

import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
from folder import export_csv_to_folder

params = dict()
params['access_token'] = 'EAAG24jaJaYIBAIZBfd4evHIXFmsW6kAoRUnClhQLgd6vNjZAnUHXKXW3kXkaLrZBUvS4LqIrFycjxM8ZAygVB1FlMF9nxHpRJXybu4ZAw1LMk7UKDXntjx22dqREoX7TZAZBdDpuCzBHc8uXFaZAZBkeqXKb4v5jgHeMIOwYZBZA9Ha4ADzHa9YkQaHO2mi1ZAJYcUNBLdybLYTCIAZDZD'        # not an actual access token
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


#transform audience_insight into dataframe
def transform_data_country(audience_insight):
    #The variables that I search for
    audience_country = []
    #Variables for Country
    country_short = []
    country_number = []

    for i in audience_insight["data"]:
        if i['name'] == "audience_country":
            for x in i['values']:
                for z in x["value"]:
                    country_short.append(z)
                    country_number.append(x['value'][z])
    audience_country = pd.DataFrame(list(zip(country_short, country_number)), columns =['Country_ID', 'Count'])
    audience_country = audience_country.sort_values(by = ['Count'],ascending=False)
    export_csv_to_folder(audience_country, 'country_data.csv')
    print(audience_country)

def transform_data_city(audience_insight):
    #The variables that I search for
    #Variables for City
    city_name = []
    region_name = []
    city_number = []
    for i in audience_insight["data"]:
        if i['name'] == "audience_city":
            for x in i['values']:
                for z in x["value"]:
                    xy = z.split(", ")
                    city_name.append(xy[0])
                    region_name.append(xy[1])
                    city_number.append(x['value'][z])

    audience_city = pd.DataFrame(list(zip(city_name, region_name, city_number)), columns =['City', 'Region', 'Count'])
    #audience_city
    audience_city = audience_city.sort_values(by = ['Count'],ascending=False)
    export_csv_to_folder(audience_city, 'cityminimal_data.csv')
    print(audience_city)

def transform_data_gender(audience_insight):
    #The variables that I search for
    #Variables for Age and Gender
    gender = []
    age_bracket = []
    age_number = []

    for i in audience_insight["data"]:
        if i['name'] == "audience_gender_age":
            for x in i['values']:
                for z in x["value"]:
                    gender_age_split = z.split(".")
                    gender.append(gender_age_split[0])
                    age_bracket.append(gender_age_split[1])
                    age_number.append(x['value'][z])
    audience_genderage = pd.DataFrame(list(zip(gender, age_bracket, age_number)), columns =['Gender', 'Age Bracket', 'Count'])
    export_csv_to_folder(audience_genderage, 'genderminimal_data.csv')
    print(audience_genderage)

target = ["country", "city", "gender"]

def get_demographics_data(url, goal):
    url = params['endpoint_base'] + params['instagram_account_id'] + '/insights'

    # Define Endpoint Parameters
    endpointParams = dict()
    endpointParams['metric'] = 'audience_city,audience_country,audience_gender_age' 
    endpointParams['period'] = 'lifetime' 
    endpointParams['access_token'] = params['access_token'] 

    # Requests Data
    data = requests.get(url, endpointParams )
    for i in goal:  
        print(i) 
        audience_insight = json.loads(data.content)
        if i == "country":
            transform_data_country(audience_insight)
        elif i == "city":
            transform_data_city(audience_insight)
        elif i == "gender":  
            transform_data_gender(audience_insight)
        else:
            print("Error")
#call method to retrieve data from API
get_demographics_data(url, target)