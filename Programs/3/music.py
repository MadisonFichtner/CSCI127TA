def longest_song():
    lib = open("music.csv",'r')
    longest = [0, 'temp'] # to save details of longest song
    song = lib.readline()
    song = lib.readline() # first song

    while song:
        info = song.replace(", ",'`').split(',')
        # if the current song is longer than the longest song
        if float(info[9]) > longest[0]:
            longest[0] = float(info[9])
            longest[1] = info[33].replace('`',", ")
        song = lib.readline()

    print("Title:", longest[1])
    print("Length to nearest second:", round(longest[0]))
    lib.close()

def songs_by_year(year):
    lib = open("music.csv",'r')
    count = 0 # number of songs in the year
    song = lib.readline()
    song = lib.readline() # first song

    while song:
        info = song.replace(", ",'`').split(',')

        # if the current song is longer than the longest song
        if year == int(info[-1].replace('\n','')):
            count += 1
        song = lib.readline()

    print("The number of songs from", year,"is", count)
    lib.close()

def all_songs_by_artist(artist):
    lib = open("music.csv",'r')
    song = lib.readline()
    song = lib.readline() # first song

    songs = []
    while song:
        info = song.replace(", ",'`').split(',')

        if artist.lower() == info[2].lower():
            songs.append(info[33].replace('`',", "))
        song = lib.readline()

    print("\nSongs In Alphabetical Order")
    print("---------------------------")
    if len(songs) == 0:
        print("There are no songs by this artist.")
    else:
        songs.sort()
        for title in songs:
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
            pass
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

main()
