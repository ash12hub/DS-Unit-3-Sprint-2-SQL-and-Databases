import pandas as pd
import sqlite3


buddy_move = pd.read_csv('buddymove_holidayiq.csv')
assert buddy_move.shape == (249, 7)
assert buddy_move.isnull().values.all() == False


buddy_move_conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
# buddy_move.to_sql('review', buddy_move_conn)

buddy_move_cursor = buddy_move_conn.cursor()

row_query = 'SELECT count(\'User Id\') from review'
rows = buddy_move_cursor.execute(row_query).fetchone()[0]
print(f'Number of Rows: {rows}\n')

nature_query = ('SELECT count(Nature) from review WHERE Nature >= 100;')
nature = buddy_move_cursor.execute(nature_query).fetchone()[0]
print(f'Users who reviewed Nature greater that 100: {nature}')

shopping_query = ('SELECT count(Shopping) from review WHERE Shopping >= 100;')
shopping = buddy_move_cursor.execute(shopping_query).fetchone()[0]
print(f'Users who reviewed Shopping greater that 100: {shopping}')

buddy_move_cursor.close()
buddy_move_conn.close()
