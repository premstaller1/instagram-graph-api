#upload csv to bigquery

from google.cloud import bigquery
import os

def upload_csv_to_bigquery(filename):
    table_id = filename.split("_")[0]
    file_path = f'data/{filename}'
    project_id = "instagram-analytics-384117"
    dataset_id = "instagramanalyticsdata"
    
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )

    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Wait for the job to complete

    print(f"CSV file {file_path} uploaded to BigQuery table {table_id}.")
    

def upload_value_to_bigquery(value, table_id, date):
    project_id = "instagram-analytics-384117"
    dataset_id = "instagramanalyticsdata"
    table_id = table_id # Replace with your desired table ID

    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Create a dictionary with the column name and value
    row = {"count": value, "date": date}

    # Insert the row into the table
    errors = client.insert_rows_json(table_ref, [row])

    if errors == []:
        print(f"Value {value} inserted into BigQuery table {table_id}.")
    else:
        print(f"Errors occurred while inserting the value into BigQuery table: {errors}")

    