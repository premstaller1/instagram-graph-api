#create function to convert a dataframe into a csv file and put it into a folder
import os
from db_upload import upload_csv_to_bigquery

def export_csv_to_folder(df, filename):
    #create a csv file from the dataframe
    folder_path = 'data'  # Replace with the actual folder path
    file_path = os.path.join(folder_path, filename)
    df.to_csv(file_path, index=False)
    upload_csv_to_bigquery(filename)
    
