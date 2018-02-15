def print_hand(hand):
    print("Cribbage Hand")
    print("-------------")
    for number in range(len(hand)):
        print("Card " + str(number + 1) + ": " + str(hand[number][0]) + " of " + hand[number][1].capitalize())

def flush(hand):
    suit = hand[0][1] # find the first suit
    for card in hand:
        # if the suits do not match, award 0 points
        if card[1] != suit:
            return 0
    return 4

def pairs(hand):
    result = 0
    if hand[0][0] == hand[1][0]:
        result += 2
    if hand[0][0] == hand[2][0]:
        result += 2
    if hand[0][0] == hand[3][0]:
        result += 2
    if hand[1][0] == hand[2][0]:
        result += 2
    if hand[1][0] == hand[3][0]:
        result += 2
    if hand[2][0] == hand[3][0]:
        result += 2
    return result

def evaluate_hand(hand):
    score = pairs(hand) + sequence(hand) + fifteens(hand) + flush(hand)
    print("Points scored:", score)
    print()

def process_hands(cribbage_input, cards_in_hand):
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

def main():
    poker_input = open("cribbage.txt", "r")
    process_hands(poker_input, 3)
    poker_input.close()

main()
