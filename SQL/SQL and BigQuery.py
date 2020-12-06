#Query SQL using Python
#using BigQuery

from google.cloud import bigquery

client = bigquery.Client() 		#establish connection
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)		#api call to fetch table

tables = list(client.list_tables(dataset))  #lists table inside dataset
for table in tables:
	print(table.table_id)

table_ref = dataset_ref.table("crime")	
table = client.get_table(table_ref)		#gets info on table crime
client.list_rows(table, max_results=5).to_dataframe()	#takes 5 lines in table and display in to_dataframe

