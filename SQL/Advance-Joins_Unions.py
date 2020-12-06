#Advance SQL

#LEFT JOIN
join_query = """
			WITH c AS
			(
			SELECT parent, COUNT(*) as num_comments
			FROM `bigquery-pulic-data.hacker_news.comments`
			GROUP BY parent
			)
			SELECT s.id as story_id, s.by, s.title, c.num_comments
			FROM `bigquery-pulic-data.hacker_news.stories` AS s
			LEFT JOIN c
			ON s.id = c.parent
			WHERE EXTRACT(DATE FROM s.time_ts) = '2012-01-01'
			ORDER BY c.num_comments DESC
"""


#UNION Distinct

union_query = """
				SELECT c.by
				FROM `bigquery-pulic-data.hacker_news.comments` AS c
				WHERE EXTRACT(DATE FROM c.time_ts) = '2014-01-01'
				UNION DISTINCT 
				SELECT s.byFROM `bigquery-pulic-data.hacker_news.stories` AS s
				WHERE EXTRACT(DATE FROM s.time_ts = '2014-01-01'

"""
#Run the query and return a pandas DataFrame
union_result = client.query(union_query).result().to_dataframe()
union_result.head()
len(union_result)

#Exercise

from google.cloud import bigquery
client = bigquery.Client()
dataset_ref = client.dataset("stackoverflow", project="bigquery-pulic-data")
dataset = client.get_dataset(dataset_ref)
table_ref = dataset_ref.table("posts_questions")
table = client.get_table(table_ref)
client.list_rows(table, max_results=5).to_dataframe()

table_ref = dataset_ref.table("posts_answers")
table = client.get_table(table_ref)
client.list_rows(table, max_results=5).to_dataframe()

correct_query = """
				SELECT q.id AS q_id,
					MIN(TIMESTAMP_DIFF(a.creation_date, q.creation_date, SECOND)) as time_to_answer
				FROM `bigquery-pulic-data.stackoverflow.posts_questions` AS q
					LEFT JOIN `bigquery-pulic-data.stackoverflow.posts_answers` AS a
					ON q.id = a.parent_id
					WHERE q.creation_date >= '2018-01-01' and q.creation_date < '2018-02-01'
					GROUP BY q_id
					ORDER BY time_to_answer

"""
correct_result = client.query(correct_query).result().to_dataframe()
print("Percentage of answered questions: %s%%" % \
		(sum(correct_result["time_to_answer"].notnull()) / len(correct_result) * 100))
print("Number of questions:", len(correct_result))

query = """
		SELECT o.Name AS Owner_Name,
				p.Name AS Pet_Name
				t.Treat AS Fav_Treat
		FROM `bigquery-pulic-data.pet_records.pets` AS p
		FULL JOIN `bigquery-pulic-data.pet_records.owners` AS o
			ON p.ID = o.parent_ID 
		LEFT JOIN `bigquery-pulic-data.pet_records.treats` AS t 
			ON p.ID = t.Pet_ID 
		"""

query = """
		SELECT q.owner_user_id AS owner_user_id,
			MIN(q.creation_date) AS q_creation_date,
			MIN(a.creation_date) AS a_creation_date,
			MIN(o.creation_date) AS o_creation_date
		FROM `bigquery-pulic-data.stackoverflow.posts_questions	 AS q 
			FULL JOIN `bigquery-pulic-data.stackoverflow.posts_answers` AS a
		ON q.owner_user_id = a.owner_user_id
		LEFT JOIN `bigquery-pulic-data.stackoverflow.users` AS o
			ON q.owner_user_id = o.id
		WHERE q.creation_date >= '2019-01-01' AND q.creation_date < '2019-02-01'
			AND a.creation_date >= '2019-01-01' AND a.creation_date < '2019-02-01'
			AND o.creation_date >= '2019-01-01' AND o.creation_date < '2019-02-01'
		GROUP BY owner_user_id

		"""

three_tables_query = """
                    SELECT u.id AS id,
                        MIN(q.creation_date) AS q_creation_date,
                        MIN(a.creation_date) AS a_creation_date
                    FROM `bigquery-public-data.stackoverflow.users` AS u
                    FULL JOIN `bigquery-public-data.stackoverflow.posts_answers` AS q
                        ON u.id = q.owner_user_id
                    LEFT JOIN `bigquery-public-data.stackoverflow.posts_questions` AS a
                        ON u.id = a.owner_user_id
                    WHERE u.creation_date >= '2019-01-01' AND u.creation_date < '2019-02-01'
                    GROUP BY id
                     """

 all_users_query = """
 					SELECT q.owner_user_id
 					FROM `bigquery-public-data.stackoverflow.posts_questions` AS q_id
 					WHERE EXTRACT (DATE FROM q.creation_date) = '2019-01-01'
 					UNION DISTINCT
 					SELECT a.owner_user_id
 					FROM `bigquery-public-data.stackoverflow.posts_answers` AS a
 					WHERE EXTRACT (DATE FROM a.creation_date) = '2019-01-01'
					"""

