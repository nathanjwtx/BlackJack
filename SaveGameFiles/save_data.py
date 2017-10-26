'''Maintain a game stats history from session to session.
Creates a file in C:/BlackJack/

N Waterman 04-18-17 v1.0
'''

import sqlite3 as sql
import os

save_file=''

def main(previous, player):
    global save_file

    if os.name == 'nt':
        # test for folder and create if missing
        if not os.path.exists('C:/BlackJack/'):
            os.mkdir('C:/BlackJack/')

        save_file = 'C:/BlackJack/game_save.sqlite'
    else:
        save_file = os.path.expanduser('~/.blackjack_game_save.sqlite')

    if not os.path.isfile(save_file):
        create_tables()
    else:
        return get_data(player)


def create_tables():
    global save_file

    # create tables on first run of game
    db = sql.connect(save_file)
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE players(player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT, bank_roll FLOAT)
    ''')
    db.commit()
    db.close()


def add_player(player):
    global save_file
    db = sql.connect(save_file)
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO players(player_name, bank_roll)
        VALUES('nathan', 50.00)
    ''')





if __name__ == '__main__':
    main(previous, player)
