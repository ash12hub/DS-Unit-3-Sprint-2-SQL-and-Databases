import pandas as pd
import psycopg2
import sqlite3

titanic = pd.read_csv('titanic.csv')
titanic.head()

# !wget https://raw.githubusercontent.com/ash12hub/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv


assert titanic.isnull().values.all() == False

titanic_conn = sqlite3.connect('titanic')
titanic_cursor = titanic_conn.cursor()
titanic.to_sql('titanic', titanic_conn)
data = titanic_cursor.execute('SELECT * FROM titanic').fetchall()

dbname = 'cayietbl'
user = 'cayietbl'
password = 'oHwmQCRV06TmwhKnv9T7nVkIjf8ZoIgx'
host = 'john.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_cursor = pg_conn.cursor()

titanic_table = '''
CREATE TABLE titanic(
    Index INT PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    AGE REAL,
    "Siblings/Spouses Aboard" INT,
    "Parents/Children Aboard" INT,
    Fare REAL)
    '''

pg_cursor.execute(titanic_table)

for item in data:
    if str(item[3]).find("'") > -1:
        continue
    pg_cursor.execute('INSERT INTO titanic VALUES ' + str(item) + ';')

pg_cursor.close()
pg_conn.commit()
pg_conn.close()
