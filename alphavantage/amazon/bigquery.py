from google.cloud import bigquery
import os

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\gcp\flawless-augury-387108-9fce49a6b23c.json"


# Create a BigQuery client
client = bigquery.Client()

# Specify the project ID, dataset ID, and table ID
project_id = 'flawless-augury-387108'
dataset_id = 'flawless-augury-387108.test_1'
table_id = 'flawless-augury-387108.test_1.table_1'

# Configure the job
job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
)

# Path to your local JSON file
file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\amazon\extracted_data_amazon.json'

# Create a job to load the data
with open(file_path, 'rb') as file:
    job = client.load_table_from_file(
        file,
        table_id,
        job_config=job_config
    )

job.result()  # Wait for the job to complete

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows into {project_id}:{dataset_id}.{table_id}")

