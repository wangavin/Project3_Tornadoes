import sqlite3

connection = sqlite3.connect('tornadograph.db')


with open('Torn_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('year', 'Content for the yr')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('mag', 'Content for the mag')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('inj', 'Content for the inj')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('fat', 'Content for the fat')
            )

connection.commit()
connection.close()
