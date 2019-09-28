import sqlite3

northwind_conn = sqlite3.connect('northwind_small.sqlite3')
northwind_cursor1 = northwind_conn.cursor()

most_expensive_query = (
                        'SELECT ProductName FROM '+
                        '(SELECT * FROM  Product ' +
                        'Order by UnitPrice DESC LIMIT 10);'
)

most_expensive = northwind_cursor1.execute(most_expensive_query).fetchall()
most_expensive_string = ''
for i in range(len(most_expensive) - 1):
    most_expensive_string = most_expensive_string + most_expensive[i][0] + ', '
most_expensive_string =  most_expensive_string + most_expensive[9][0]

"""10 MostExpensive Items"""
print(f'The 10 most expensive items are: {most_expensive_string}.\n')


birth_dates = northwind_cursor1.execute('SELECT BirthDate FROM Employee;').fetchall()
hire_dates = northwind_cursor1.execute('SELECT HireDate FROM Employee;').fetchall()


def split_dates(dates):
    years = []
    months = []
    days = []
    for i in range(len(dates)):
        split_date = dates[i][0].split('-')
        years.append(int(split_date[0]))
        months.append(int(split_date[1]))
        days.append(int(split_date[2]))
    
    return years, months, days


def get_average(list):
    return int(sum(list) / len(list))


brith_years, birth_months, birth_days = split_dates(birth_dates)
hire_years, hire_months, hire_days = split_dates(hire_dates)

age = []
for i in range(len(brith_years)):
    year = (hire_years[i] - brith_years[i])
    if(hire_months[i] < birth_months[i]):
        year -= 1
    elif(hire_months[i] == birth_months[i]):
        if(hire_days[i] < birth_days[i]):
            year -= 1
    age.append(year)

"""Average age of employees at hire"""
print(f'The Average Age of Employees at the time of hire is {get_average(age)}.\n')


employee_cities = northwind_cursor1.execute('SELECT City FROM Employee;').fetchall()
cities = []
city_agess = []

for i in range(len(employee_cities)):
    employee_cities[i] = employee_cities[i][0]
    if employee_cities[i] not in cities:
        cities.append(employee_cities[i])
        city_agess.append([age[i]])
    else:
        index = cities.index(employee_cities[i])
        city_agess[index].append(age[i])

"""Average age of employees at hire per city"""
for i in range(len(cities)):
    print(f'The Average Age of Employees from {cities[i]}' +
          f'at the time of hire is {get_average(city_agess[i])}.\n\n')

northwind_cursor1.close()

northwind_cursor2 = northwind_conn.cursor()

product_supplier_price_query = ('SELECT Product.ProductName, Supplier.CompanyName FROM Product ' +
                                'INNER JOIN Supplier ON Product.SupplierId = Supplier.id ' +
                                'ORDER BY Product.UnitPrice DESC ' +
                                'LIMIT 10;')

"""10 MostExpensive Items with their Suppliers"""
print(northwind_cursor2.execute(product_supplier_price_query).fetchall())

northwind_cursor2.close()
northwind_conn.close()
