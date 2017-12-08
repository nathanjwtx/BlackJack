import random as r
import GameFiles.deck as d
import GameFiles.player as p
import GameFiles.game_logic as gl


def black_jack():

    dealer = p.Player()
    players = []
    player_count = int(input("Enter the number of players: "))

    for x in range(0, player_count):
        name = input("Enter the name of Player " + str(x+1) + ": ")
        name = p.Player(name)
        players.append(name)
    gl.play_hand(players, player_count, dealer)


if __name__ == "__main__":
    black_jack()
