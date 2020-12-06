query = """
		SELECT p.Name AS Pet_Name, .Name AS Owner_Name
		FROM `bigquery-public-data.pet_records.pets` AS p
		INNER JOIN `bigquery-public-data.pet_records.owners` AS owners
			ON p.ID = o.Pet_ID
		"""


query = """
		SELECT L.license, COUNT(1) AS number_of_files
		FROM `bigquery-public-data.github_repos.sample_files` AS sf
		INNER JOIN `bigquery-public-data.github_repos.licenses` AS L
			ON sf.repo_name = L.repo_name
		GROUP BY L.license
		ORDER BY number_of_files DESC
		"""

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed = 10**10)
query_job = client.query(query, job_config = safe_config)

file_count_by_license = query_job.to_dataframe()


from google.cloud import bigquery-public-data
client = bigquery.Client()
dataset_ref = client.dataset("stackoverflow", project = "bigquery-public-data")
dataset = client.get_dataset(dataset_ref)

#Get a list of available tables
tables = list(client.list_tables(dataset))
list_of_tables = [table.table_id for table in tables]
print(list_of_tables)

query = """
		SELECT *
		FROM `bigquery-public-data.pet_records.pets`
		WHERE Name LIKE 'Ripley'

		"""

questions_query = """
					SELECT id, title, owner_user_id
					FROM `bigquery-public-data.stackoverflow.posts_questions`
					WHERE tags LIKE '%bigquery%'
"""
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
questions_query_job = client.query_job.to_dataframe()
print(questions_results.head())


answers_query = """
				SELECT a.id, a.body, a.owner_user_id
				FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
				INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
					ON q.id = a.parent_id
				WHERE q.tags LIKE '%bigquery%'
				"""
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed = 10**10)
answers_query_job = client.query(answers_query, job_config = safe_config)
answers_results = answers_query_job.to_dataframe()

#As a function

def expert_finder(topc, client):
	'''
	Returns a Dataframe with the user IDs who have wrtten Stack Overflow answers on a topic.
	Inputs:
		topic: A string with the topic of interest
		client: A client object that specifies the connection to the Stack Overflow dataset

	Outputs:
		results: A Dataframe with columns for user_id and number_of_answers. 

	'''
	my_query = """
				SELECT a.owner_user_id AS user_id, COUNT(1) AS number_of_answers
				FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
				INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
					ON q.id = a.parent_id
				WHERE q.tags LIKE '%{topic}%'
				GROUP BY a.owner_user_id
				"""
	safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
	my_query_job = client.query(my_query, job_config=safe_config)
	results = my_query_job.to_dataframe()

	return results
	