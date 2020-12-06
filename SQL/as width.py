query = """
		WITH Seniors AS
		(
			SELECT ID, Name
			FROM `bigquery-public-data.pet_records.pets`
			WHERE Years_old >5
		)
		SELECT ID
		FROM Seniors
		"""


# Query to select the number of transactions per date, sorted by date
query_with_CTE = """
				 WITH time AS
				 (
				 	SELECT DATE(block_timestamp) AS trans_date
				 	FROM `bigquery-public-data.crypto_bitcoin.transactions`
				 )
				 SELECT COUNT(1) AS transactions,
				 		trans_date
				 FROM time
				 GROUP BY trans_date
				 ORDER BY trans_date
				 """	