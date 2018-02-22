def calculate_attendance(playname, filename):
    bway = open(filename,'r')
    play = bway.readline()
    play = bway.readline() # first song

    atten = 0
    while play:
        info = play.split(',')
        # if the current play matches the given play name
        if info[7].lower() == playname:
            atten += int(info[0])
        play = bway.readline()
    return atten

def calculate_revenue(playname, filename):
    bway = open(filename,'r')
    play = bway.readline()
    play = bway.readline() # first song

    rev = 0
    while play:
        info = play.split(',')
        # if the current play matches the given play name
        if info[7].lower() == playname:
            rev += int(info[4])
        play = bway.readline()
    return rev

def main():
    play_name = input("Please enter the name of a play: ")
    play_name = play_name.lower()
    attendance = calculate_attendance(play_name, "broadway.csv")
    print("Total attendance is", "{:,d}".format(attendance))
    revenue = calculate_revenue(play_name, "broadway.csv")
    print("Total revenue is", "${:,d}".format(revenue))

main()
