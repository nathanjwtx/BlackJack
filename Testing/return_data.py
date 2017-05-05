import sqlite3 as sql


def get_data(player):
    # return list of saved players details
    db = sql.connect('c:/blackjack/game_save.sqlite')
    cursor = db.cursor()
    players = cursor.execute('''
        SELECT * FROM players
        WHERE player_name = :player_name
    ''', {"player_name": player.upper()})
    return players

if __name__ == '__main__':
    get_data(player)
