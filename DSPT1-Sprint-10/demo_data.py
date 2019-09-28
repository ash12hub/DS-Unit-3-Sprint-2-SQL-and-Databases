import sqlite3

db_conn = sqlite3.connect('demo_data.sqlite3')
db_cursor = db_conn.cursor()

create_table = 'CREATE TABLE demo (s VARCHAR(1), x INTEGER, y INTEGER);'
db_cursor.execute(create_table)

data_entry_1 = 'INSERT INTO demo VALUES(\'g\', 3, 9);'
data_entry_2 = 'INSERT INTO demo VALUES(\'v\', 5, 7);'
data_entry_3 = 'INSERT INTO demo VALUES(\'f\', 8, 7);'
db_cursor.execute(data_entry_1)
db_cursor.execute(data_entry_2)
db_cursor.execute(data_entry_3)

db_conn.commit()

count_rows_query = 'SELECT count(*) FROM demo;'
count_rows = db_cursor.execute(count_rows_query).fetchone()[0]
"""Number of rows"""
print(f'Total number of rows: {count_rows}')

count_at_least_5_query = ('SELECT count(*) FROM ' +
                          '(SELECT x, y FROM demo ' +
                          'WHERE x >= 5 and y >= 5);'
                          )
count_at_least_5 = db_cursor.execute(count_at_least_5_query).fetchone()[0]
"""Rows where X and Y are at least 5"""
print(f'Total number of rows with x and y at least 5: {count_at_least_5}')

count_distinct_y_query = 'SELECT count(DISTINCT y) FROM demo;'
count_distinct_y = db_cursor.execute(count_distinct_y_query).fetchone()[0]
"""Number of Unique Values in y"""
print(f'Unique values of y: {count_distinct_y}')

db_cursor.close()
db_conn.close()
