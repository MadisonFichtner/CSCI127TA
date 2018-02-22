# --------------------------------------
# CSCI 127, Lab 6
# February 22, 2018
# Your Name
# --------------------------------------

# The missing functions go here.

# --------------------------------------

def main():
    play_name = input("Please enter the name of a play: ")
    play_name = play_name.lower()
    attendance = calculate_attendance(play_name, "broadway.csv")
    print("Total attendance is", "{:,d}".format(attendance))
    revenue = calculate_revenue(play_name, "broadway.csv")
    print("Total revenue is", "${:,d}".format(revenue))

# --------------------------------------

main()
