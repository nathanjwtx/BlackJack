import sqlite3 as sql

db = sql.connect('C:/BlackJack/game_save.sqlite')
cursor = db.cursor()

cursor.execute('''
    DELETE from players
''')
