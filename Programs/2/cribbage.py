
# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def process_hands(cribbage_input, cards_in_hand):

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

# --------------------------------------

def main():
    poker_input = open("cribbage.txt", "r")
    process_hands(poker_input, 3)
    poker_input.close()

# --------------------------------------

main()
