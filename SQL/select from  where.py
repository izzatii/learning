from google.cloud import bigquery

#create  a client object
client = bigquery.Client()

#construct a reference to the "openaq" dataset
dataset_ref = clienr.dataset("openaq", project = "bigquery-public-data")

#API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#List all the tables in the "openaq" dataset
tables = list(client.list_tables(dataset))

#Print names of all tables in the dataset
for table in tables:
	print(table.table_id)


#Construct a reference to the "global_air_quality" table
table_ref = dataset_ref.table("global_air_quality")

#API request - fetch the table
table = client.get_table(table_ref)

#Preview the first five ines of the "global_air_quality" table
client.list_rows(table, max_results = 5).to_dataframe()

#Query to select all the items from the "city" column where the "country" column is US
query = """
		SELECT city
		FROM `bigquery-public-data.openaq.global_air_quality`
		WEHERE country = 'US'
		"""

#set up the query
query_job = client.query(query)

#API request - run the query, and return a pandas to_dataframe
us_cities = query_job.to_dataframe()

#What five cities have the most measurement?
us_cities.city.value_counts().head()

#more queries
query = """
		SELECT city, country
		FROM `bigquery-public-data.openaq.global_air_quality

		WHERE country = 'US'
		"""

#to select all columns
query = """
		SELECT *
		FROM `bigquery-public-data.openaq.global_air_quality

		WHERE country = 'US'
		"""

#to check how much data query will scan
# Create a QueryJobConfig object to estimate the size of query without running it
dry_run_config = bigquery.QueryJobConfig(dry_run=True)

#API request - dry run query to estimate costs
dry_run_query_job = client.query(query, job_config=dry_run_config)

print("This query will process {} bytes".format(dry_run_query_job.total_bytes_processed))

#limit how much data willing to scan
#only run the query if its less than 1MB
ONE_MB = 1000*1000
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed = ONE_MB)

#set up the query
safe_query_job = client.query(query, job_config=safe_config)

#API request - try to run the query, and return a pandas DataFrame
safe_query_job.to_dataframe()

