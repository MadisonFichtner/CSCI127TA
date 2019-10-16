def flush(cvals):
    pass

def score_4_of_a_kind(cvals):
    if cvals[0] == cvals[1] and cvals[0] == cvals[2] and cvals[0] == cvals[3]: # 3 of a kind
        return 6
    return 0

def score_3_of_a_kind(cvals):
    if cvals[0] == cvals[1] and cvals[0] == cvals[2]: # 3 of a kind
        return 6
    return 0

def score_pair(cvals):
    if cvals[0] == cvals[1] or cvals[1] == cvals[2]: # pair
        return 2
    return 0

def score_sequence(cvals):
    if cvals[1] == (cvals[0] + 1) and cvals[2] == (cvals[1] + 1): # sequence
        return 3
    return 0

def score_fifteen(cvals):
    cfif = 0 # the number of 15s that can be made
    if (cvals[0] + cvals[1] + cvals[2]) == 15:
        cfif += 1
    if cvals[0] + cvals[1] == 15:
        cfif += 1
    if cvals[1] + cvals[2] == 15:
        cfif += 1
    if cvals[0] + cvals[2] == 15:
        cfif += 1
    return 2 * cfif # award points for each 15

def evaluate_hand(hand_as_list):
    cvals = [] # keep track of the values of the cards
    for card in hand_as_list:
        cvals.append(card[0]) # keep track of the card's value
    cvals.sort() # arrange the values in numerical order

    print("Points scored:",max(score_3_of_a_kind(cvals),score_pair(cvals))+score_sequence(cvals)+score_fifteen(cvals),"\n")

def print_hand(hand, number):
    print("Cribbage Hand\n-------------")
    i = 1
    for card in hand:
        print("Card",i,":",card[0],"of",card[1].title())
        i += 1

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

def main():
    poker_input = open("cribbage.txt", "r")
    process_hands(poker_input, 5)
    poker_input.close()

main()
