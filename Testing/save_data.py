'''Maintain a game stats history from session to session.
Creates a file in C:/BlackJack/

N Waterman 04-18-17 v1.0
'''

import sqlite3 as sql
import os


def main(player):
    # test for folder and create if missing
    if not os.path.exists('C:/BlackJack/'):
        os.mkdir('C:/BlackJack/')
    else:
        if not os.path.isfile('C:/BlackJack/game_save.sqlite'):
            create_tables()
        else:
            return get_data(player)


def create_tables():
    # create tables on first run of game
    db = sql.connect('C:/BlackJack/game_save.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE players(player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT, bank_roll FLOAT)
    ''')
    db.commit()
    db.close()


def get_data(player):
    # return list of saved players details
    db = sql.connect('c:/blackjack/game_save.sqlite')
    cursor = db.cursor()
    players = cursor.execute('''
        SELECT player_id, player_name, bank_roll FROM players
        WHERE player_name = :player_name
    ''', {"player_name": player})
    return players

if __name__ == '__main__':
    main(player)
