from peewee import *

album = input('enter albums: ')
conn = SqliteDatabase('chinook.db')
cursor = conn.cursor()
cursor.execute(f'SELECT  Name FROM tracks WHERE (SELECT AlbumId FROM albums WHERE Title = "{album}") = AlbumId;')
results = cursor.fetchall()
print(results)
conn.close()

