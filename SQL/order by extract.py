query = """
		SELECT ID, Name, Animal
		FROM `bigquery-public-data.pet_records.pets`
		ORDER BY ID
		"""

query = """
		SELECT ID, Name, Animal
		FROM `bigquery-public-data.pet_records.pets`
		ORDER BY Animal
		"""

query = """
		SELECT Name, EXTRACT (DAY from Date) AS DAY
		FROM `bigquery-public-data.pet_records.pets_with_date`
		"""

query = """
		SELECT COUNT(consecutive_number) AS num_accidents,
				EXTRACT(DAYOFWEEK FROM timestamp_of_crash) AS day_of_week
		FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
		GROUP BY day_of_week
		ORDER BY num_accidents DESC
		"""

country_spend_pct_query = """
						  SELECT country_name,
						  		 AVG(value) AS avg_ed_spending_pct
						  FROM `bigquery-public-data.world_bank_intl_education.international_eduction`
						  WHERE indicator_code = 'SE.XPD.TOTL.GD.ZS'
						  		AND year >= 2010 AND year <= 2017
						  GROUP BY country_name
						  ORDER BY avg_ed_spending_pct DESC
						  """
safe_config = bigquey.QueryJobConfig(maximum_bytes_billed=10**10)
country_spend_pct_query_job = client.query(country_spend_pct_query, job_config = safe_config)
country_spending_results = country_spend_pct_query_job.to_dataframe()
print(country_spending_results.head())

'''
1. You should have one row for each indicator code.
2. The columns in your results should be called indicator_code, indicator_name, and num_rows.
3. Only select codes with 175 or more rows in the raw database (exactly 175 rows would be included).
4. To get both the indicator_code and indicator_name in your resulting DataFrame, you need to include both in your SELECT statement (in addition to a COUNT() aggregation). This requires you to include both in your GROUP BY clause.
5. Order from results most frequent to least frequent.
'''

code_count_query = """
                    SELECT indicator_code, indicator_name,COUNT(1) AS num_rows
                    FROM `bigquery-public-data.world_bank_intl_education.international_education`
                    WHERE year = 2016
                    GROUP BY indicator_name, indicator_code
                    HAVING COUNT(1) >= 175
                    ORDER BY COUNT(1) DESC

                    """

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
code_count_query_job = client.query(code_count_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
code_count_results = code_count_query_job.to_dataframe()

# View top few rows of results
print(code_count_results.head())