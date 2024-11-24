import duckdb
duckdb.sql("INSTALL httpfs;LOAD httpfs;") # required extension
#Test
#df = duckdb.sql(f"SELECT name FROM 'hf://datasets/do-me/foursquare_places_100M/foursquare_places.parquet' WHERE country = 'BR' LIMIT 1 ").df()

df = duckdb.sql(f"SELECT * FROM 'hf://datasets/do-me/foursquare_places_100M/foursquare_places.parquet' WHERE country = 'BR' ").df()
df.to_csv('output_brazil.csv', index=False)

print("Data exported!")