from csv import reader

# longest_song searches the music.csv file for the longest song in the file
def longest_song():
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True) # reader to read CSV
    next(libreader) # skip the column names

    longest = [0, 'temp'] # details of longest song
    for song in libreader:
        if float(song[9]) > longest[0]: # if song's length is greater than the longest
            longest[0] = float(song[9])
            longest[1] = song[33]

    print("Title:", longest[1])
    print("Length to nearest second:", round(longest[0]))
    lib.close()

# songs_by_year outputs the number of songs in the music.csv file for a given year
def songs_by_year(year):
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True) # reader to read CSV
    next(libreader) # skip the column names

    count = 0 # number of songs listed in year
    for song in libreader:
        if year == int(song[-1]): # if the song's year is year
            count += 1

    print("The number of songs from", year,"is", count)
    lib.close()

# all_songs_by_artist alphabetically prints all song names for a given artist
def all_songs_by_artist(artist):
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True) # reader to read CSV
    next(libreader) # skip the column names

    arsongs = [] # list to hold all the artist's songs
    for song in libreader:
        if artist.lower() == song[2].lower(): # if the song's artist is artist
            arsongs.append(song[33])

    # pretty print the songs in arsongs
    print("\nSongs In Alphabetical Order")
    print("---------------------------")
    if len(arsongs) == 0:
        print("There are no songs by this artist.")
    else:
        arsongs.sort()
        for title in arsongs:
            print(title)
    print("---------------------------")

    lib.close()

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. You choose something that is interesting and non-trivial.")
    print("5. Quit.")

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            print("Not yet implemented.")
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

main()
