import sqlite3 as sql


save_file = 'game_save.sqlite'
db1 = sql.connect(save_file)
cursor = db1.cursor()

cursor.execute('''
        CREATE TABLE players(player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT, bank_roll FLOAT)
    ''')
db1.commit()

cursor.execute('''
        INSERT INTO players(player_name, bank_roll)
        VALUES('nathan', 50.00)
    ''')

db.commit()
db.close()
