# --------------------------------------
# CSCI 127, Lab 3
# February 1, 2018
# Your Name
# --------------------------------------

def remove_builtin(sentence):
    return "" 

def remove_iterative(sentence):
    return ""

def remove_recursive(sentence):
    return ""

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        print()
        print("Removing all whitespace from the sentence")
        print("-----------------------------------------")
        print("Using replace   = |" + remove_builtin(sentence) + "|")
        print("Using iteration = |" + remove_iterative(sentence) + "|")
        print("Using recursion = |" + remove_recursive(sentence) + "|")
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
