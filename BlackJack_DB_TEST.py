
import SaveGameFiles.save_data as game_save
import GameFiles.deck as d
import GameFiles.player as p

def black_jack():

    dealer = p.Player()
    players = []
    player_count = int(input("Enter the number of players: "))

    for x in range(0, player_count):
        player_name = input("Enter the name of Player " + str(x+1) + ": ")
        name = p.Player(player_name)
        played_before = input('Do you have a saved game? Y or N')
        players.append(name)
        if played_before.upper() == 'Y':
            previous_winnings = load_save(player_name)
            # need to rewrite this and adjust the class
            players[x].money = previous_winnings
    play_hand(players, player_count, dealer)


def load_save(player_name):
    a = game_save.main(player_name)
    for z in a:
        return z[0]


def play_hand(players, player_count, dealer):
    # make new deck for each hand to ensure odds are same
    deck = d.Deck()
    deck.make_deck()
    # make empty hands
    for x in range(0, len(players)):
        players[x].set_stick('no')
        players[x].make_hand()
        # print('New hand: ' + str(players[x].get_hand()))
        opening = int(input("How much is opening bet? $"))
        players[x].set_money(-1 * opening)
        players[x].set_bet(opening)
        print(players[x].get_name() + " you have #" +
              str(players[x].get_money) + " remaining")

    # deal cards to hands
    for z in range(0, 2):
        for y in range(0, len(players)):
            players[y].update_hand(deck.deal_card())

    # display initial hands for players and dealer
    for x in range(0, player_count):
        display_hand(players[x])
        score = hand_total(players[x].get_hand(), 0, False)
        if score == 21:
            print(players[x].get_name() + " has BlackJack!")
            players[x].set_score(21)
            players[x].set_stick("yes")
        elif int(score) > 21:
            print("Busted!")
            players[x].set_stick("bust")
        else:
            players[x].set_score(score)
            print(players[x].get_name() + " has " + str(score))

    dealer.make_hand()
    dealer.update_hand(deck.deal_card())
    display_dealer(dealer.get_hand())
    dealer.set_score(hand_total(dealer.get_hand(), 0, True))

    # deal next cards for players
    for p in range(0, player_count):
        stick = players[p].get_stick
        while stick == "no":
            # print(players[p].get_stick())
            # if hand_total(players[p].get_hand()) > 21:
            if players[p].get_score() > 21:
                players[p].set_stick("bust")
                print(players[p].get_name() + " is bust")
                break
            elif input(players[p].get_name() +
                       " would you like to stick? Y or N \n").lower() != "y":
                players[p].update_hand(deck.deal_card())
                display_hand(players[p])
                new_score = str(hand_total(players[p].get_hand(),
                                           players[p].get_score(), False))
                players[p].set_score(int(new_score))
                print(players[p].get_name() + " has " + new_score)
            else:
                players[p].set_stick("yes")
                break

    # update dealers hand
    bust_count = 0
    for p in range(0, player_count):
        if players[p].get_stick == 'bust':
            bust_count += 1
    if bust_count != player_count:
        while dealer.get_score() < 17:
            dealer.update_hand(deck.deal_card())
            display_dealer(dealer.get_hand())
            dealer.set_score(hand_total(dealer.get_hand(), dealer.get_score(),
                                        True))
            print("Dealer has: " + str(dealer.get_score()))
            if 17 < dealer.get_score() <= 21:
                dealer.set_stick("yes")
                print("Dealer sticks on " + str(dealer.get_score()))
                # winners(player_count, players, dealer)
                break
            elif dealer.get_score() > 21:
                dealer.set_stick("bust")
                print("Dealer has busted")
                break

    # remove a player if they run out of money
    for p in range(0, player_count):
        if int(winners(p, players, dealer)) <= 0:
            print(players[p].get_name() + " you are out of the game")
            players.remove(players[p])
            player_count -= 1
        else:
            # print(winners(p, players, dealer))
            print(players[p].get_name() + ' ' + players[p].get_result +
                  '\nNew balance is: $' + str(players[p].get_money))

    if player_count == bust_count:
        print('Thanks for playing')
    elif input("Would you like to play again? Y or N").upper() == "Y":
        play_hand(players, player_count, dealer)
    else:
        print("Thanks for playing")


def winners(p, players, dealer):
    # determine wager result
    # for p in range(0, player_count):
    if players[p].get_stick == 'bust':
        # print(players[p].get_name() + " loses")
        players[p].set_result('lost')
    elif dealer.get_stick == "bust" and players[p].get_stick != "bust":
        if players[p].get_score() == 21 and len(players[p].get_hand()) == 2:
            # print(players[p].get_name() + "1 you have won: $" + str(2 * players[p].get_bet))
            players[p].set_money(2 * players[p].get_bet)
            players[p].set_result('wins')
        else:
            players[p].set_money(1.5 * players[p].get_bet)
            players[p].set_result('wins')
            # return players[p].get_name() + "2 you have won: $" + str(1.5 * players[p].get_bet)
            # print(players[p].get_money())
    elif players[p].get_score() > dealer.get_score():
        # print(players[p].get_name() + "3 you have won: $" + str(1.5 * players[p].get_bet))
        players[p].set_money(1.5 * players[p].get_bet)
        players[p].set_result('wins')
        # print(players[p].get_money())
    elif players[p].get_score() == dealer.get_score():
        # print("This round is a draw")
        players[p].set_money(players[p].get_bet)
        players[p].set_result('draw')
    else:
        # print(players[p].get_name() + " loses")
        players[p].set_result('lost')
    return players[p].get_money


def display_dealer(dealer):

    if len(dealer) == 1:
        print("Dealer, your face card is: " + dealer[0])
    else:
        print("Dealer, your next card is: " + dealer[len(dealer)-1])


def display_hand(players):

    hand = players.get_hand()
    print(players.get_name() + " your cards are: ")
    for y in range(0, len(hand)):
        print(hand[y])


def hand_total(hand, score, dealer):
    # print(hand)
    # can i rework this to be more efficient?
    if len(hand) == 2:
        print("hand_total: " + str(score))
        if dealer:
            # score = 0
            # for x in range(0, 2):
            #     score += int(card_value(hand[x]))
                score += int(card_value(hand[len(hand)-1]))
        else:
            for x in range(0, 2):
                score += int(card_value(hand[x]))
    elif len(hand) == 1:
        score += int(card_value(hand[0]))
    else:
        if hand[len(hand) - 1][:1] == "A" and score > 10:
            score += 1
        else:
            score += int(card_value(hand[len(hand) - 1]))
    return score


def card_value(card):
    if card[:1] in ('J', 'Q', 'K') or len(card) == 3:
        value = 10
    elif card[:1] == 'A':
        ace = input("A is 1 or 11? ")
        value = int(ace)
    else:
        value = card[:1]
    # print("Value: " + str(value))
    return value


black_jack()
