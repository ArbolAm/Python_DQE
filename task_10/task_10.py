import sqlite3
import sys
sys.path.insert(1, 'C:\\Users\\amiran_arbolishvili\\PycharmProjects\\python_DQE\\Python_DQE\\task_5')

import task_5


agent = task_5.NewsAgent("News_sql", "Exciting News About Python Classes!")
agent.create_news()

with sqlite3.connect('task_10.db') as connection:
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM news')
    result = cursor.fetchall()
    print(result)




