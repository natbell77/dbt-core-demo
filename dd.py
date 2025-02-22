import duckdb

con = duckdb.connect('dev.duckdb')
result = con.sql('SELECT * FROM my_first_dbt_model')
print(result)
