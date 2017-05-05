import sqlite3 as sql

db = sql.connect('C:/BlackJack/game_save.sqlite')
cursor = db.cursor()

# cursor.execute('''
#     DELETE FROM players
# ''')

cursor.execute('UPDATE players SET player_name = "NATHAN" WHERE player_id = 22')

db.commit()
db.close()
