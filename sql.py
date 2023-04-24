import sqlite3
conn = sqlite3.connect('food_log.db')
cur = conn.cursor()
cur.execute('SELECT * FROM food')
data = cur.fetchall()
print(data)

