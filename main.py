import psycopg2
from psycopg2 import Error
from data import Data

data = Data()

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="salarydb")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    l = [1, 6, 11, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52]
    rowcount = 1
    for j in range(0, data.df.keys().size):
        print(data.df.keys()[j])
        for i in range(0, data.df.index.size):
            if i in l:
                print(data.df.index[i], data.df.values[i][j])
                row = (rowcount, int(data.df.keys()[j]), data.df.index[i], int(data.df.values[i][j]))
                cursor.execute('INSERT INTO dashboard_annualsalary(id, year, economic_activity, total) '
                               'VALUES (%s,%s,%s,%s)', row)
                connection.commit()
                rowcount += 1
        print()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
