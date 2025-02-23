import duckdb

table_list = ["Dates", "Employees", "OrderItems", "Orders", "Products", "Stores", "Suppliers", "customers"]

con = duckdb.connect('dev.duckdb')

def show_tables():
    result = con.sql('SHOW ALL TABLES')
    return result

def remove_table(table_name):
    result = con.sql(f'DROP TABLE {table_name}')
    print(result)

def truncate_all_tables(truncate_list):
    for table in truncate_list:
        con.sql(f'TRUNCATE TABLE {table}')

#remove_table("orders")

#truncate_all_tables(table_list)

result = con.sql(
    '''
    DESCRIBE OrderItems
    '''
)
print(result)

duckdb.disconnect('dev.duckdb')
