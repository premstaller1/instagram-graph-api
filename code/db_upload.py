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
    
#upload_csv_to_bigquery('city_data.csv')