import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"exemple{i}@gmail.com", f"{i*10}", f"{1000}"))#
for i in range(1, 11, 2):
        cursor.execute("SELECT balance FROM Users")
        cursor.execute(f"UPDATE Users SET balance = + 500 WHERE id = ?", (i,))
        print(i)
for i in range(0, 11, 3):
    i += 1
    cursor.execute(f"DELETE FROM Users WHERE id = ?", (i,))
    print(i)
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(f'{user[0]} | {user[1]} | {user[2]} | {user[3]}')

connection.commit()
connection.close()

