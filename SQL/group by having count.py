#Query to select comments that received more than 10 replies
query_popular = """
				SELECT parent, COUNT(1) AS NumPosts
				FROM `bigquery-public-data.hacker_news.comments
				GROUP BY parent
				HAVING COUNT(id) > 10
				"""

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10*10)
query_job = client.query(query_popular, job_config = safe_config)

popular_comments = query_job.to_dataframe()
popular_comments.head()