# Из списка детей записываем данные в DB а потом заполняем CSV файл этими данными
# Код закоментирован, но блоки подписаны какой функционал они выполняют
import sqlite3, csv

connection = sqlite3.connect('DB_CSV_children.db')
cursor = connection.cursor()

    #Создаем список детей

chldr_list = [('Михаил','Васнецов','35','Москва'),
              ('Петя','Петушков','21','Казань'),
               ('Алёша','Баранов','10','Тула')]

    # Вставкой заполняем созданные поля базы данных из списка детей

# cursor.executemany("INSERT INTO children VALUES (?,?,?,?)", chldr_list)
# connection.commit()

#     # создаем таблицу с полями

# cursor.execute("""
#                 CREATE TABLE children
#                 (name text, lastname text, age text, born_in text)
#                 """)

    #Записываем в csv файл данные из базы данных

# with open('test.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     for row in cursor.execute("SELECT * FROM children ORDER BY name"):
#         writer.writerow(row)


    # Смотрим всю базу данных
sql = "SELECT * FROM children"
cursor.execute(sql)
print(cursor.fetchall())

