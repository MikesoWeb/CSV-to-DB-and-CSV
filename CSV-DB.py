import sqlite3, csv

connection = sqlite3.connect('DB_CSV_children.db')
cursor = connection.cursor()

# Читаем csv файл и берем построчно оттуда данные,
# записывая их в базу данных

with open('test.csv', encoding='utf-8') as file:
    writer = csv.reader(file)
    cursor.executemany("INSERT INTO children VALUES (?,?,?,?)", writer)
    connection.commit()

# Просматриваем всю базу данных построчно
sql = "SELECT * FROM children"
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)