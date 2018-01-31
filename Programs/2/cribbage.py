def evaluate_hand(hand):
    points = 0
    print("Points scored:",points,"\n")

def print_hand(hand):
    print("Cribbage Hand\n-------------")
    i = 1
    for card in hand:
        print("Card",i,":",card[0],"of",card[1].title())
        i += 1

def process_hands(cribbage_input, cards_in_hand):
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for _ in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

def main():
    poker_input = open("cribbage.txt", "r")
    process_hands(poker_input, 3)
    poker_input.close()

main()
