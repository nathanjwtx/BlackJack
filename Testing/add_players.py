import sqlite3 as sql

db = sql.connect('C:/BlackJack/game_save.sqlite')
cursor = db.cursor()

cursor.execute('''
    INSERT INTO players(player_name, bank_roll) 
    VALUES('nathan', 50.00)
''')

db.commit()
db.close()
