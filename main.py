import psycopg2
from psycopg2 import Error
from data import Data

import requests
import bs4

data = Data()


response = requests.get("https://уровень-инфляции.рф/таблицы-инфляции")
tree = bs4.BeautifulSoup(response.text, 'html.parser')
t = tree.select('td', {'class':'text-right'})
index = 27
l1 = [index + 14, index + 14 * 2, index + 14 * 3, index + 14 * 4, index + 14 * 5, index + 14 * 6]
coff = []
count = 0
for item in tree.select('td', {'class':'text-right'}):
    if count in l1:
        coff.append(item.text)
    count += 1
    if len(coff) > 7:
        break
coff.reverse()
print(coff) #инфляция с 2017 года

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
    for j in range(1, data.df.keys().size):
        #print(data.df.keys()[j])
        print(float(coff[j - 1]) / 100 + 1)
        for i in range(0, data.df.index.size):
            if i in l:
                #print(data.df.index[i], data.df.values[i][j])
                row = (rowcount, int(data.df.keys()[j]), data.df.index[i], int(data.df.values[i][j]) / (float(coff[j - 1]) / 100 + 1) - int(data.df.values[i][j - 1]))
                print(row)
                cursor.execute('INSERT INTO dashboard_difference(id, year, economic_activity, total) '
                'VALUES (%s,%s,%s,%s)', row)
                connection.commit()
                rowcount += 1

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
