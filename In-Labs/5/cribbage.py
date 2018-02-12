def print_hand(hand):
    print("Cribbage Hand")
    print("-------------")
    for number in range(len(hand)):
        print("Card " + str(number + 1) + ": " + str(hand[number][0]) + " of " + hand[number][1].capitalize())

def pairs(hand):
    result = 0
    if hand[0][0] == hand[1][0]:
        result += 2
    if hand[0][0] == hand[2][0]:
        result += 2
    if hand[1][0] == hand[2][0]:
        result += 2
    return result

def sequence(hand):
    hand.sort()
    if hand[0][0] + 1 == hand[1][0] and hand[1][0] + 1 == hand[2][0]:
        return 3
    else:
        return 0

def fifteens(hand):
    result = 0
    card_one = hand[0][0]
    card_two = hand[1][0]
    card_three = hand[2][0]

    if card_one + card_two + card_three == 15:
        result +=2
    if card_one + card_two == 15:
        result += 2
    if card_one + card_three == 15:
        result += 2
    if card_two + card_three == 15:
        result += 2

    return result

def evaluate_hand(hand):
    score = pairs(hand) + sequence(hand) + fifteens(hand)
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
