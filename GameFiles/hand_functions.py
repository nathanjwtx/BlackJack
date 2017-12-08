'''
Functions for display and calculating hands
'''


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

    if len(hand) == 2:
        print("hand_total: " + str(score))
        if dealer:
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
    return value
