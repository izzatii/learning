#Analytics Functions or Analytic Window Functions or Window Functions

query = """
		SELECT *
			AVG(time) OVER(
						PARTITION BY id
						ORDER BY date
						ROWS BETWEEN 1 PRECEDIGN AND CURRENT ROW
						) as avg_time
		FROM `bigquery-public-data.runners_train_time`

"""

num_trips_query = """
				WITH trips_by_day as
				(
				SELECT DATE(start_date) AS trip_date,
					COUNT(*) as num_trips
				FROM `bigquery-public-data.san_francisco.bikeshare_trips`
				WHERE EXTRACT(YEAR FROM start_date) = 2015
				GROUP BY trip_date
				)
				SELECT *,
					SUM(num_trips)
						OVER (
							ORDER BY trip_date
							ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
							) AS cumulative_trips
					FROM trips_by_day
				"""

num_trips_result = client.query(num_trips_query).result().to_dataframe()
num_trips_result.head()

start_end_query = """
					SELECT bike_number,
						TIME(start_date) AS trip_time,
						FIRST_VALUE(start_station_id)
							OVER (
								PARTITION BY bike_number
								ORDER BY start_date
								ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
								) AS first_station_id,
						LAST_VALUE(end_station_id)
							OVER (
								PARTITION BY bike_number
								ORDER BY start_date
								ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
								) AS last_station_id,
						start_station_id,
						end_station_id
					FROM `bigquery-public-data.san_francisco.bikeshare_trips`
					WHERE DATE(start_date) = '2015-10-25'
					"""

start_end_result = client.query(start_end_query).result().to_dataframe()
start_end_result.head()

from google.cloud import bigquery

#Create a client object
client = bigquery.Client()

#Construct a reference to the "chicago_taxi_trips" dataset
dataset_ref = client.dataet("chicago_taxi_trips", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#Construct a reference to the "taxi_trips" table
table_ref = dataset_ref.table("taxi_trips")

# API request - fetch the table
table = client.get_table(table_ref)

#Preview the first five lines of the table
client.list_rows(table, max_results=5).to_dataframe()


avg_num_trips_query = """
						WITH trips_by_day AS
						(
						SELECT DATE(trip_start_timestamp) AS trip_date,
							COUNT(*) as num_trips
						FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
						WHERE trip_start_timestamp >= '2016-01-01' AND trip_start_timestamp < '2018-01-01'
						GROUP BY trip_date
						ORDER BY trip_date
						)
						SELECT trip_date,
							AVG(num_trips)
							OVER (
								ORDER BY trip_date
								ROWS BETWEEN 15 PRECEDING AND 15 FOLLOWING
								) AS avg_num_trips
						FROM trips_by_day
						"""

#Using Rank()

trip_number_query = """
					SELECT pickup_community_area,
						trip_start_timestamp,
						trip_end_timestamp,
						RANK()
							OVER(
								PARTITION BY pickup_community_area
								ORDER BY trip_start_timestamp
								) AS trip_number 
					FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
					WHERE DATE(trip_start_timestamp) = '2017-05-01'
					"""

trip_number_result = client.query(trip_number_query).result().to_dataframe()

#Calculating timelapse

break_time_query = """
					SELECT taxi_id,
						trip_start_timestamp,
						trip_end_timestamp,
						TIMESTAMP_DIFF(
							trip_start_timestamp,
							LAG(trip_end_timestamp,1)
							OVER (
								PARTITION BY taxi_id
								ORDER BY trip_start_timestamp),
							MINUTE) as prev_break
					FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
					WHERE DATE(trip_start_timestamp) = '2017-05-01'
					"""