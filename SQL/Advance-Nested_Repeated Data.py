#Nested and Repeated Data

#Nested data

query = """
		SELECT Name AS Pet_Name,
			Toy.Name AS Toy_Name,
			Toy.Type AS Toy_Type
		FROM `bigquery-public-data.pet_records.pets_and_toys`
		"""

#Repeated Data

query = """
		SELECT Name AS Pet_Name,
			Toy_Type
		FROM `bigquery-public-data.pet_records.pets_and_toys_type`,
			UNNEST(Toys) AS Toy_Type
		"""

#Nested and Repeated Data

query = """
		SELECT Name AS Pet_Name,
			t.Name AS Toy_Name,
			t.Type AS Toy_Type
		FROM `bigquery-public-data.pet_records.more_pets_and_toys`,
			UNNEST(Toys) AS t
		"""

# Query to count number of transactions per browser

query = """
		SELECT device.browser AS device_browser,
			SUM(totals.transactions) as total_transactions
		FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
		GROUP BY device_browser
		ORDER BY total_transactions
		"""
result = client.query(query).result().to_dataframe()
result.head()

#Query to determine most popular landing point on the website

query = """
		SELECT hits.page.pagePath as path,
			COUNT(hits.page.pagePath) as counts
		FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
			UNNEST(hits) as hits
		WHERE hits.type="PAGE" and hits.hitNumber=1
		GROUP BY path
		ORDER BY counts DESC
		"""
result = client.query(query).result().to_dataframe()
result.head()

#Query to find individuals with the most commits

max_commits_query = """
					SELECT committer.name AS committer_name,
						COUNT(*) AS num_commits
					FROM `bigquery-public-data.github_repos.sample_commits`
					WHERE committer.date > '2016-01-01' AND committer.date <'2017-01-01'
					GROUP BY committer_name
					ORDER BY num_commits DESC
					"""


#Query to find popular language

pop_lang_query = """
				SELECT l.name AS language_name, COUNT(*) AS num_repos
				FROM `bigquery-public-data.github_repos.languages`,
					UNNEST(language) AS l
				GROUP BY language_name
				ORDER BY num_repos DESC
				"""

#Query to check which language used in the repo with most languages

all_langs_query = """
				SELECT l.name, l.bytes
				FROM `bigquery-public-data.github_repos.languages`,
					UNNEST(language) as l
				WHERE repo_name = 'polyrabbit/polyglot'
				ORDER BY l.bytes
"""